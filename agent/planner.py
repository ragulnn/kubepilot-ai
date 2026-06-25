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

        try:
            return json.loads(text)

        except Exception:

            print("\nInvalid JSON returned by planner:\n")
            print(text)

            return {
                "tool": "finish"
            }

    def next_action(self, question, observations, context):
        executed_tools = []

        for obs in observations:
            executed_tools.append(obs["tool"])


        prompt = f"""
Question:
{question}

Cluster Context:

{json.dumps(context, indent=2)}

Already executed tools:

{executed_tools}

Previous observations:

{json.dumps(observations, indent=2)}
"""
        action = self._call_llm(prompt)

        if (
            action["tool"] in executed_tools
            and action["tool"] != "finish"
        ):
            return {
                "tool": "finish"
            }


        return action

    def fix_action(self, action, error):

        prompt = f"""
The following Kubernetes action is invalid.

Action:

{json.dumps(action, indent=2)}

Validation error:

{error}

Return a corrected Kubernetes action.

Return ONLY valid JSON.
"""

        return self._call_llm(prompt)
