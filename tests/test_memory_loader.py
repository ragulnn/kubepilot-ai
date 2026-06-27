from agent.memory import Memory

memory = Memory()

print("=" * 60)
print("ALL INCIDENTS")
print("=" * 60)

for incident in memory.load_all_incidents():

    print(incident["question"])

print()

print("=" * 60)
print("LATEST INCIDENT")
print("=" * 60)

print(
    memory.load_latest_incident()
)
