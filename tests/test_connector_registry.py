from connectors.default_registry import registry

print("=" * 60)
print("Connector Registry")
print("=" * 60)

for connector in registry.connectors:

    print(connector.name)

    print("Capabilities:", connector.capabilities)

    print("-" * 40)
