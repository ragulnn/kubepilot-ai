from agent.memory import Memory

memory = Memory()

fingerprint = {

    "root_cause":"OOMKilled",

    "symptom":"CrashLoopBackOff",

    "namespace":"default",

    "resource_name":"nginx",

    "severity":"High"
}

matches = memory.find_similar(
    fingerprint
)

print()

print("=" * 60)
print("SIMILAR INCIDENTS")
print("=" * 60)

for match in matches:

    print()

    print("Score :", match["score"])

    print("Question :")

    print(match["incident"]["question"])
