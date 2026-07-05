from agents.default_registry import registry

print("Registered Agents")
print("-" * 40)

for name in registry.list():

    agent = registry.get(name)

    print(agent.name)
    print(agent.capabilities)
    print()
