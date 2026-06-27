from agent_server.router import RequestRouter
from agent_server.registry import ConnectorManager
from agent_protocol.request import AgentRequest


router = RequestRouter(
    ConnectorManager().registry()
)


request = AgentRequest(

    cluster="default",

    request_id="1",

    user="local",

    evidence_type="pods",

)

response = router.handle(request)

print(response)
