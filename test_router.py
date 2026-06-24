from agent.router import Router

router = Router()

questions = [

    "show all pods",

    "list services",

    "get namespaces",

    "why is nginx crashing",

    "my website is down",

    "restart deployment nginx",

    "scale deployment to 3",

    "delete pod nginx"

]

for question in questions:

    print("=" * 50)

    print(question)

    print("Intent:", router.route(question))
