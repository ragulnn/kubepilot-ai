from fastapi import FastAPI

from agent_server.health import HealthMonitor
from agent_protocol.registration import AgentRegistration
from pydantic import BaseModel

from agent.graph import graph


class InvestigationRequest(BaseModel):

    question: str
registered_agents = {}
app = FastAPI()

health = HealthMonitor()


@app.get("/")
def root():

    return {

        "application": "Kubepilot Agent",

        "version": "1.0.0",

    }


@app.get("/health")
def healthy():

    return health.healthy()
@app.post("/register")
def register(agent: AgentRegistration):

    registered_agents[agent.cluster] = {

        "hostname": agent.hostname,

        "ip": agent.ip,

        "version": agent.version,

    }

    return {

        "success": True,

        "message": "Agent registered",

        "cluster": agent.cluster,

    }
@app.post("/investigate")
def investigate(request: InvestigationRequest):

    state = {

        "question": request.question,

        "observations": [],

        "current_action": None,

        "investigation": None,

        "resources": {},

        "evidence": [],

        "knowledge_graph": None,

        "root_causes": [],

        "confidence": 0.0,

        "recommended_action": None,

        "answer": "",

        "fingerprint": None,

        "memory_match": None,

        "finished": False,

        "guard_reason": "",

    }

    result = graph.invoke(state)

    return result["answer"]
