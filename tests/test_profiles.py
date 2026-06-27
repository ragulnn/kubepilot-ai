from agent.profile_selector import ProfileSelector

selector = ProfileSelector()

questions = [

    "Show all pods",

    "Why is nginx crashing?",

    "List services",

    "Application is slow",

]

for q in questions:

    print("=" * 50)

    print(q)

    profile = selector.choose(q)

    for request in profile:

        print("-", request.type)
