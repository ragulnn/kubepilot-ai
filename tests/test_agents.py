from agents.planner_agent import PlannerAgent
from agents.discovery_agent import DiscoveryAgent
from agents.evidence_agent import EvidenceAgent

state = {

    "question": "Why is nginx crashing?"

}

planner = PlannerAgent()

discovery = DiscoveryAgent()

evidence = EvidenceAgent()

state = planner.run(state)

print()

print("Workflow")

print(state["workflow"])

state = discovery.run(state)

print()

print("Resources")

print(state["resources"])

state = evidence.run(state)

print()

print("Responses")

print(len(state["responses"]))
