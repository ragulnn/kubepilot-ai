from planning_engine.executor import InvestigationExecutor

print("=" * 60)
print("Investigation Planner")
print("=" * 60)

executor = InvestigationExecutor()

confidence = 0.52

collected = [

    "metrics",

]

while True:

    plan = executor.execute(

        confidence,

        collected,

    )

    print(plan)

    if plan["completed"]:

        break

    collected.append(

        plan["next"]

    )

    confidence += 0.18
