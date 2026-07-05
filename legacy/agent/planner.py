from ollama import chat
import json
import time

from agent.prompts import PLANNER_PROMPT
from utils.config import PLANNER_MODEL

AVAILABLE_TOOLS = [
    "pods",
    "logs",
    "describe",
    "events",
    "services",
    "nodes",
    "deployments",
    "ingress",
    "namespaces",
    "pv",
    "pvc",
    "configmap",
    "kubectl",
    "secrets",
]


class Planner:

    def _call_llm(self, prompt: str) -> dict:

        start = time.time()

        response = chat(
            model=PLANNER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": PLANNER_PROMPT,
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        elapsed = time.time() - start

        print(f"\nPlanner Ollama Call : {elapsed:.2f} sec")

        text = response["message"]["content"]

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        try:
            return json.loads(text)

        except Exception:

            print("\n⚠ Invalid JSON returned by planner:\n")
            print(text)

            return {
                "tool": "finish"
            }

    def next_action(
        self,
        question,
        observations,
        history,
        resources,
        context,
        investigation=None,
    ):

        executed_tools = []

        for obs in observations:

            if isinstance(obs, dict):

                tool = obs.get("tool")

                if tool:
                    executed_tools.append(tool)

        prompt = f"""
Question

{question}

====================================================

Cluster Context

{json.dumps(context, indent=2)}

====================================================

Executed Tools

{json.dumps(executed_tools, indent=2)}

====================================================

Investigation History

{history}

====================================================

Structured Kubernetes Resources

{json.dumps(resources, indent=2)}

====================================================

Current Investigation Status

{json.dumps(investigation, indent=2)}

====================================================

You are an expert Kubernetes Site Reliability Engineer.

Your job is to decide the NEXT BEST Kubernetes action.

Available Kubernetes tools

{json.dumps(AVAILABLE_TOOLS, indent=2)}

Rules

1. Analyze the question, history and investigation.

2. Choose EXACTLY ONE Kubernetes tool.

When selecting describe, logs or events ALWAYS use the structured Kubernetes resources.

Never invent resource names.

If no resource exists, choose another tool or return:

{{
    "tool":"finish"
}}

3. A tool MAY be repeated if additional evidence can still be collected.

4. If confidence is already above 95% or no useful investigation remains, return:

{{
    "tool":"finish"
}}

5. Return ONLY valid JSON.

Example

{{
    "tool":"pods",
    "namespace":"default",
    "reason":"Check pod health."
}}
"""

        print(
            f"Planner Prompt Size : {len(prompt)} characters"
        )

        action = self._call_llm(prompt)

        if not isinstance(action, dict):
            return {"tool": "finish"}

        tool = action.get("tool")

        if tool is None:
            return {"tool": "finish"}

        if tool != "finish" and tool not in AVAILABLE_TOOLS:

            print(f"\n⚠ Unknown tool: {tool}")

            return {"tool": "finish"}

        if tool in executed_tools and tool != "finish":

            print(
                f"\n⚠ Planner selected '{tool}' again."
            )

        return action

    def fix_action(self, action, error):

        prompt = f"""
The following Kubernetes action is invalid.

Action

{json.dumps(action, indent=2)}

Validation Error

{error}

Return ONLY corrected JSON.
"""

        return self._call_llm(prompt)

    def create_plan(self, question):

        return self.next_action(
            question=question,
            observations=[],
            history="",
            resources={},
            context={},
            investigation=None,
        )
