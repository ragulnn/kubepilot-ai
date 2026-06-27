from agent.fingerprint import FingerprintGenerator

generator = FingerprintGenerator()

report = {

    "affected_resource":"nginx",

    "namespace":"default",

    "symptom":"CrashLoopBackOff",

    "root_cause":"OOMKilled",

    "confidence":0.95,

    "severity":"High",

    "evidence":[
        "Exit Code 137"
    ]
}

observations = [

    {
        "tool":"pods"
    },

    {
        "tool":"logs"
    },

    {
        "tool":"describe"
    }
]

fingerprint = generator.generate(
    report,
    observations,
    cluster="kind"
)

print(fingerprint)
