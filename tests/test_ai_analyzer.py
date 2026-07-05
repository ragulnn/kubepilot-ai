from analysis_engine.ai_analyzer import AIAnalyzer

print("=" * 60)
print("AI Analyzer")
print("=" * 60)

aggregated = {

    "sources":[

        "prometheus",

        "loki",

        "tempo",

        "kubernetes",

    ],

    "summaries":[

        "Memory pressure",

        "OOMKilled",

        "PaymentService Exception",

        "CrashLoopBackOff",

    ],

    "findings":[

        "Memory 98%",

        "Restart Count 8",

        "OOMKilled",

    ],

}

analysis = AIAnalyzer().analyze(

    aggregated

)

print()

print(analysis)
