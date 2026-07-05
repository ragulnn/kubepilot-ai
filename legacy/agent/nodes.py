from datetime import datetime

from utils.logger import Timer
from workflow_engine.router import WorkflowRouter
from workflow_engine.executor import WorkflowExecutor
# ---------------------------------------------------------
# Core Components
# ---------------------------------------------------------

from agent.planner import Planner
from agent.executor import Executor
from agent.analyzer import Analyzer
from agent.context import ClusterContext
from agent.summarizer import Summarizer

# ---------------------------------------------------------
# Resource Layer
# ---------------------------------------------------------

from agent.resource_extractor import ResourceExtractor
from agent.resource_resolver import ResourceResolver

# ---------------------------------------------------------
# Evidence Layer
# ---------------------------------------------------------

from agent.evidence_store import EvidenceStore
from agent.evidence_extractor import EvidenceExtractor
from agent.evidence_deduplicator import EvidenceDeduplicator

# ---------------------------------------------------------
# Knowledge Graph
# ---------------------------------------------------------

from agent.knowledge_graph import KnowledgeGraph
from agent.graph_builder import GraphBuilder
from agent.relationship_builder import RelationshipBuilder

# ---------------------------------------------------------
# Confidence
# ---------------------------------------------------------

from agent.evidence_quality import EvidenceQualityEngine
from agent.confidence_engine import ConfidenceEngine

# ---------------------------------------------------------
# Root Cause
# ---------------------------------------------------------

from agent.root_cause_engine import RootCauseEngine
from agent.root_cause_ranker import RootCauseRanker
from agent.root_cause_summary import RootCauseSummary

# ---------------------------------------------------------
# Investigation Strategy
# ---------------------------------------------------------

from agent.investigation_strategy import InvestigationStrategy
from agent.tool_selector import ToolSelector
from agent.investigation_state import InvestigationState

# ---------------------------------------------------------
# Memory
# ---------------------------------------------------------

from agent.fingerprint import FingerprintGenerator
from agent.memory import Memory
from agent.verifier import MemoryVerifier

# ---------------------------------------------------------
# Investigation Guard
# ---------------------------------------------------------

from agent.investigation_guard import InvestigationGuard

# =========================================================
# Global Components
# =========================================================

planner = Planner()
executor = Executor()
analyzer = Analyzer()

summarizer = Summarizer()

resource_extractor = ResourceExtractor()
resolver = ResourceResolver()

evidence_store = EvidenceStore()
evidence_extractor = EvidenceExtractor()
deduplicator = EvidenceDeduplicator()

knowledge_graph = KnowledgeGraph()
graph_builder = GraphBuilder()
relationship_builder = RelationshipBuilder()

quality_engine = EvidenceQualityEngine()
confidence_engine = ConfidenceEngine()

root_cause_engine = RootCauseEngine()
root_cause_ranker = RootCauseRanker()
root_cause_summary = RootCauseSummary()

strategy = InvestigationStrategy()
tool_selector = ToolSelector()
investigation_state = InvestigationState()

fingerprint_generator = FingerprintGenerator()
memory = Memory()
verifier = MemoryVerifier()

guard = InvestigationGuard()


# =========================================================
# Planner Node
# =========================================================

def planner_node(state):
    router = WorkflowRouter()

    executor = WorkflowExecutor()
    with Timer("Planner Node"):

        print("\n" + "=" * 60)
        print("🚀 Planner Node")
        print("=" * 60)

        question = state["question"]
        workflow = router.route(question)

        if workflow:

            print()

            print("=" * 60)

            print("🚀 Workflow Engine")

            print("=" * 60)

            print()

            responses = executor.execute(

                workflow,

                question,

            )

            observations = []

            for response in responses:

                observations.append(

                    {

                        "tool": response.request.type,

                        "summary": response.message,

                        "raw": response.evidence,

                    }

                )

            return {

                **state,

                "observations": observations,

                "finished": True,

            }
        print(f"Question : {question}")

        print("\nLoading cluster context...")

        context = ClusterContext().load()

        print("✅ Context Loaded")

        history = summarizer.summarize_history(
            state["observations"]
        )

        resources = summarizer.collect_resources(
            state["observations"]
        )

        print("\nCollected Resources")
        print(resources)

        action = planner.next_action(
            question=question,
            observations=state["observations"],
            history=history,
            resources=resources,
            context=context,
            investigation=state.get("investigation"),
        )

        print("\nPlanner Decision")
        print(action)

        action = resolver.resolve(
            action,
            resources,
        )

        print("\nResolved Action")
        print(action)

        if action.get("tool") != "finish":

            investigation_state.add(
                action["tool"]
            )

        return {

            "current_action": action,

            "resources": resources,

        }
# =========================================================
# Executor Node
# =========================================================

def executor_node(state):

    with Timer("Executor Node"):

        print("\n" + "=" * 60)
        print("🚀 Executor Node")
        print("=" * 60)

        action = state["current_action"]

        print(f"Executing : {action}")

        # -------------------------------------------------
        # Execute Kubernetes Tool
        # -------------------------------------------------

        raw_output = executor.execute(action)

        # -------------------------------------------------
        # Summarize Tool Output
        # -------------------------------------------------

        summary = summarizer.summarize(
            action["tool"],
            raw_output,
        )

        # -------------------------------------------------
        # Extract Structured Resources
        # -------------------------------------------------

        resources = resource_extractor.extract(
            action["tool"],
            raw_output,
        )

        print("\nExtracted Resources")

        print(resources)

        # -------------------------------------------------
        # Convert Resources into Evidence
        # -------------------------------------------------

        evidence = evidence_extractor.extract(
            action["tool"],
            resources,
        )

        print()

        print(f"Evidence Extracted : {len(evidence)}")

        # -------------------------------------------------
        # Deduplicate Evidence
        # -------------------------------------------------

        added = 0

        skipped = 0

        for item in evidence:

            item.confidence = quality_engine.score(
                item
            )

            if deduplicator.exists(
                evidence_store,
                item,
            ):

                skipped += 1

                print(
                    f"Skipping duplicate evidence : "
                    f"{item.resource}"
                )

                continue

            evidence_store.add(item)

            added += 1

        print()

        print(
            f"Evidence Added    : {added}"
        )

        print(
            f"Evidence Skipped : {skipped}"
        )

        # -------------------------------------------------
        # Current Evidence Store
        # -------------------------------------------------

        print()

        print("Evidence Store")

        print(
            evidence_store.summary()
        )

        # -------------------------------------------------
        # Build Observation
        # -------------------------------------------------

        observation = {

            "step": len(
                state["observations"]
            ) + 1,

            "tool": action["tool"],

            "reason": action.get(
                "reason",
                "Planner selected this tool.",
            ),

            "summary": summary,

            "resources": resources,

            "raw": raw_output,

            "timestamp": datetime.now().isoformat(),

        }

        observations = (
            state["observations"]
            + [observation]
        )

        print()

        print("✅ Tool Executed")

        return {

            "observations": observations,

            "resources": resources,

            "evidence": evidence_store.all(),

        }

# =========================================================
# Analyzer Node
# =========================================================

def analyzer_node(state):

    with Timer("Analyzer Node"):

        print("\n" + "=" * 60)
        print("🚀 Analyzer Node")
        print("=" * 60)

        # -------------------------------------------------
        # Build Knowledge Graph
        # -------------------------------------------------

        graph_builder.build(
            knowledge_graph,
            evidence_store.all(),
        )

        relationship_builder.build(
            knowledge_graph,
        )

        print()

        print("Knowledge Graph")

        knowledge_graph.print_graph()

        print()

        print("Knowledge Graph Summary")

        print(
            knowledge_graph.summary()
        )

        # -------------------------------------------------
        # Calculate Confidence
        # -------------------------------------------------

        confidence = confidence_engine.calculate(
            evidence_store
        )

        print()

        print(
            f"Calculated Confidence : {confidence:.2f}"
        )

        # -------------------------------------------------
        # Root Cause Detection
        # -------------------------------------------------

        root_causes = root_cause_engine.detect(
            evidence_store
        )

        ranked = root_cause_ranker.rank(
            root_causes
        )

        root_summary = root_cause_summary.summarize(
            ranked
        )

        print()

        print("Detected Root Causes")

        print(root_causes)

        print()

        print("Primary Root Cause")

        print(root_summary)

        # -------------------------------------------------
        # Investigation Strategy
        # -------------------------------------------------

        missing = strategy.missing(
            root_summary["root_cause"],
            evidence_store,
        )

        recommendation = tool_selector.next_tool(
            missing
        )

        print()

        print("Missing Evidence")

        print(missing)

        print()

        print("Recommended Tool")

        print(recommendation)

        # -------------------------------------------------
        # Analyzer
        # -------------------------------------------------

        report = analyzer.analyze(
            question=state["question"],
            observations=state["observations"],
            evidence_store=evidence_store,
            knowledge_graph=knowledge_graph,
            confidence=confidence,
        )

        print()

        print("✅ Analysis Complete")

        # -------------------------------------------------
        # Memory
        # -------------------------------------------------

        fingerprint = fingerprint_generator.generate(
            report=report,
            observations=state["observations"],
            cluster="kind",
        )

        print()

        print("Searching Memory...")

        matches = memory.find_similar(
            fingerprint
        )

        verified_match = None

        if matches:

            best = matches[0]

            verification = verifier.verify(
                fingerprint,
                best["incident"]["fingerprint"],
            )

            if verification["verified"]:

                verified_match = {

                    "score": best["score"],

                    "verification": verification,

                    "question": best["incident"]["question"],

                }

                print(
                    "✅ Previous incident verified"
                )

        memory.save_incident(

            question=state["question"],

            fingerprint=fingerprint,

            report=report,

            observations=state["observations"],

        )

        print("✅ Investigation saved")

        # -------------------------------------------------
        # Investigation Guard
        # -------------------------------------------------

        finished, reason = guard.should_finish(

            question=state["question"],

            report=report,

            observations=state["observations"],

        )
        print("\n========== Investigation Guard ==========")
        print(f"Finished : {finished}")
        print(f"Reason    : {reason}")
        print("=========================================\n")
        print()

        print("Investigation Guard")

        print(reason)

        return {

            "answer": report,

            "investigation": report,

            "confidence": confidence,

            "knowledge_graph": knowledge_graph,

            "root_causes": ranked,

            "recommended_action": recommendation,

            "fingerprint": fingerprint,

            "memory_match": verified_match,

            "finished": finished,

            "guard_reason": reason,

        }
