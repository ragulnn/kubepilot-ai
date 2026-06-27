from agent_protocol.request import AgentRequest
from agent_protocol.response import AgentResponse

request = AgentRequest(
    cluster="default",
    request_id="123",
    user="ragul",
    evidence_type="pods",
    keyword="nginx",
)

print(request)

response = AgentResponse(
    request_id="123",
    cluster="default",
    success=True,
    connector="kubernetes",
    evidence=["nginx-pod"],
)

print(response)
