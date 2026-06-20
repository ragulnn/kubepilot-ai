from ollama import chat
import json

from agent.prompts import PLANNER_PROMPT


class Planner:

    def plan(self, question):

        response = chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "system",
                    "content": PLANNER_PROMPT
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        text = response["message"]["content"]

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)
