from agent.investigation_mode import InvestigationMode

mode = InvestigationMode()

questions = [

    "Show all pods",

    "List services",

    "Why is nginx crashing?",

    "Cluster health",

    "Debug my deployment",

]

for q in questions:

    print(q)

    print(mode.detect(q))

    print("-" * 40)
