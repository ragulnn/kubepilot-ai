from verification_engine.verifier import AIVerifier

print("=" * 60)
print("AI Verification")
print("=" * 60)

analysis = {

    "root_cause": "Memory Exhaustion",

    "critical_evidence": [

        "Memory 98%",

        "OOMKilled",

        "Restart Count 8",

        "CrashLoopBackOff",

    ],

}

result = AIVerifier().verify(
    analysis
)

print()

print(result)
