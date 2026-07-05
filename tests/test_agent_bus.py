from agent_bus.bus import AgentBus

bus = AgentBus()

bus.publish(

    "workflow",

    {

        "type": "pod"

    }

)

print(bus.topics())

print(bus.get("workflow"))

bus.clear()

print(bus.topics())
