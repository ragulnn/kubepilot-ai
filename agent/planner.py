from ollama import chat
import json

from agent.prompts import PLANNER_PROMPT
from utils.config import PLANNER_MODEL


class Planner:

    def _call_llm(self, prompt):

        response = chat(
            model=PLANNER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": PLANNER_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        text = response["message"]["content"]

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    def plan(self, question):
        return self._call_llm(question)

    def next_action(self, question, observations):

        prompt = f"""
Question:
{question}

Previous observations:
{observations}

You are investigating a Kubernetes cluster.

Choose ONLY ONE next Kubernetes tool.

If more investigation is required return:

{{
    "tool": "pods"
}}

If enough information has been collected return:

{{
    "tool": "finish"
}}

Return ONLY valid JSON.
"""

        return self._call_llm(prompt)
