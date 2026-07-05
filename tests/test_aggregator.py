from agent_bus.bus import AgentBus
from agents.aggregator_agent import AggregatorAgent

bus = AgentBus()

bus.publish(

    "responses",

    "kubernetes"

)

bus.publish(

    "responses",

    "prometheus"

)

bus.publish(

    "responses",

    "loki"

)

state = {}

agent = AggregatorAgent()

agent.bus = bus

agent.run(state)

print(state["evidence"])

print(bus.get("evidence"))
