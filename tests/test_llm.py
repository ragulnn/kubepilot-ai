from llm.client import LLMClient

print("=" * 60)
print("LLM Test")
print("=" * 60)

client = LLMClient()

response = client.generate(

    """
Memory Usage: 98%

Restart Count: 8

Logs:
OOMKilled

Trace:
PaymentService Exception
"""
)

print()

print(response.content)
