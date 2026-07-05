from ollama import chat
import json
import time

from agent.analyzer_rules import RAW_REQUIRED_TOOLS
from agent.report_schema import REPORT_SCHEMA
from agent.root_cause_engine import RootCauseEngine
from agent.root_cause_ranker import RootCauseRanker
from agent.root_cause_summary import RootCauseSummary
from utils.config import ANALYZER_MODEL


class Analyzer:

    def __init__(self):

        self.root_cause_engine = RootCauseEngine()
        self.root_cause_ranker = RootCauseRanker()
        self.root_cause_summary = RootCauseSummary()

    def analyze(
        self,
        question,
        observations,
        evidence_store=None,
        knowledge_graph=None,
        confidence=None,
    ):

        summaries = []
        raw_evidence = []

        for obs in observations:

            if "summary" in obs:
                summaries.append(obs["summary"])

            if (
                obs.get("tool") in RAW_REQUIRED_TOOLS
                and "raw" in obs
            ):
                raw_evidence.append(
                    {
                        "tool": obs["tool"],
                        "output": obs["raw"],
                    }
                )

        evidence = []

        if evidence_store:

            evidence = [
                {
                    "type": e.type,
                    "resource": e.resource,
                    "namespace": e.namespace,
                    "value": e.value,
                    "confidence": e.confidence,
                    "source": e.source_tool,
                }
                for e in evidence_store.all()
            ]

        graph_summary = {}

        if knowledge_graph:
            graph_summary = knowledge_graph.summary()

        root_causes = []
        root_summary = {}

        if evidence_store:

            root_causes = self.root_cause_engine.detect(
                evidence_store
            )

            ranked = self.root_cause_ranker.rank(
                root_causes
            )

            root_summary = self.root_cause_summary.summarize(
                ranked
            )

        prompt = f"""
You are an expert Kubernetes Site Reliability Engineer.

Question

{question}

====================================================

Investigation Summary

{json.dumps(summaries, indent=2)}

====================================================

Evidence

{json.dumps(evidence, indent=2)}

====================================================

Knowledge Graph

{json.dumps(graph_summary, indent=2)}

====================================================

Detected Root Causes

{json.dumps(root_causes, indent=2)}

====================================================

Primary Root Cause

{json.dumps(root_summary, indent=2)}

====================================================

Detailed Kubernetes Evidence

{json.dumps(raw_evidence, indent=2)}

====================================================

{REPORT_SCHEMA}

Rules

1. Use the detected root causes.

2. Prefer structured evidence over raw kubectl output.

3. Use raw evidence only if required.

4. Do NOT invent Kubernetes resources.

5. If evidence is insufficient,
set requires_manual_review=true.

6. Return ONLY valid JSON.
"""

        print(
            f"Analyzer Prompt Size : {len(prompt)} characters"
        )

        start = time.time()

        response = chat(
            model=ANALYZER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        elapsed = time.time() - start

        print(f"\nAnalyzer Ollama Call : {elapsed:.2f} sec")

        text = response["message"]["content"]

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        try:

            report = json.loads(text)

        except Exception:

            print("\n⚠ Invalid JSON returned by analyzer:\n")
            print(text)

            report = {
                "root_cause": "Unknown",
                "confidence": 0.0,
                "symptom": "",
                "evidence": [],
                "recommended_fix": [],
                "requires_manual_review": True,
            }

        if root_summary:

            report["root_cause"] = root_summary.get(
                "root_cause",
                report.get("root_cause"),
            )

        if confidence is not None:

            report["confidence"] = confidence

        return report
