from ollama import chat


def analyze_cluster(report: str):

    prompt = f"""
You are a Senior Kubernetes Site Reliability Engineer.

Analyze the following Kubernetes troubleshooting report.

Return:

1. Root Cause

2. Evidence

3. Suggested Fix

4. kubectl commands to verify

Report:

{report}
"""

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
