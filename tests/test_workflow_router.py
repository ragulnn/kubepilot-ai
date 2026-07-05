from workflow_engine.router import WorkflowRouter

router = WorkflowRouter()

questions = [

    "Why is nginx crashing?",

    "Deployment unavailable",

    "PVC Pending",

    "Random kubernetes question",

]

for q in questions:

    print()

    print(q)

    print(router.route(q))
