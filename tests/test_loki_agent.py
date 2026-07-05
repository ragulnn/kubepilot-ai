from agents.default_registry import registry

agent = registry.get("loki")

state = {}

state = agent.run(state)

print()

print(state["loki"].source)

print(state["loki"].success)

print(len(state["loki"].evidence))
