from agent.classifier import QuestionClassifier

classifier = QuestionClassifier()

questions = [

    "Show all pods",

    "List services",

    "Get namespaces",

    "Why is nginx crashing?",

    "Investigate deployment failure",

    "Analyze CrashLoopBackOff"
]

for q in questions:

    print(f"\nQuestion: {q}")

    print(
        classifier.classify(q)
    )
