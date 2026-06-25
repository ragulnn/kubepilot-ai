from agent.router import Router

router = Router()

questions = [
    "show pods",
    "list services",
    "why is nginx crashing",
    "delete pod nginx"
]

for question in questions:

    intent = router.route(question)

    print("=" * 50)
    print("Question :", question)
    print("Intent   :", intent)
