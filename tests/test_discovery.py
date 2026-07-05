from resource_engine.discovery import ResourceDiscovery

engine = ResourceDiscovery()

matches = engine.discover(
    "Investigate nginx"
)

print()

for resource in matches:

    print(

        resource["name"],

        resource["match_score"]

    )
