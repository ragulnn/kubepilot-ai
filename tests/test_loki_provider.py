from providers.registry import TOOLS

tool = TOOLS["loki"]

logs = tool.run(

    namespace="monitoring"

)

print()

print("Logs:", len(logs))

for log in logs[:5]:

    print(log["log"])
