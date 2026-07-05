from planning_engine.executor import InvestigationExecutor

executor = InvestigationExecutor()

question = "Why is nginx pod restarting?"

confidence = 0.45

collected = []

while True:

    plan = executor.execute(

        question,

        confidence,

        collected,

    )

    print(plan)

    if plan["completed"]:

        break

    collected.append(

        plan["next"]

    )

    confidence += 0.20
