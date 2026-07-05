from agents.default_registry import registry

print()

print("Registered Agents")

print("-" * 40)

for agent in registry.list():

    print(agent)
