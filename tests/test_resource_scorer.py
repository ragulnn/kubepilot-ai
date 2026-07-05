from resource_engine.scorer import ResourceScorer

scorer = ResourceScorer()

resources = [

    "frontend",

    "frontend-v2",

    "frontend-blue",

    "frontend-79fd78",

    "backend",

    "redis",

]

for resource in resources:

    score = scorer.score(
        "frontend",
        resource,
    )

    print(f"{resource:20} {score}")
