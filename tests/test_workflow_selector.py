from workflow_engine.selector import WorkflowSelector

selector = WorkflowSelector()

questions = [

    "Why is nginx crashing?",

    "Deployment unavailable",

    "PVC Pending",

    "Ingress not working",

    "Show pods",

    "Random Kubernetes question",

]

for q in questions:

    workflow = selector.select(q)

    print()

    print(q)

    print(workflow)
