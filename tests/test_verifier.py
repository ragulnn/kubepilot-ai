from agent.verifier import MemoryVerifier

verifier = MemoryVerifier()

current = {

    "root_cause":"OOMKilled",

    "symptom":"CrashLoopBackOff",

    "resource_name":"nginx",

    "namespace":"default"
}

previous = {

    "root_cause":"OOMKilled",

    "symptom":"CrashLoopBackOff",

    "resource_name":"nginx",

    "namespace":"default"
}

result = verifier.verify(
    current,
    previous
)

print(result)
