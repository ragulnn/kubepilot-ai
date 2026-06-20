from ollama import chat


class Analyzer:

    def analyze(self, question, observations):

        prompt = f"""
Question:

{question}

Investigation Results:

{observations}

Explain:

1. Root Cause

2. Evidence

3. Fix
"""

        response = chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
