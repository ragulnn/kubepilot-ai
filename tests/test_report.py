from agent.analyzer import Analyzer

analyzer = Analyzer()

observations = [
    {
        "tool": "pods",
        "summary": {
            "running": 9,
            "crashloop": 1,
            "failed": 0
        },
        "raw": ""
    }
]

result = analyzer.analyze(
    "Why is nginx restarting?",
    observations
)

print(type(result))
print(result)
