from adaptive_engine.controller import InvestigationController

controller = InvestigationController()

question = "Why is nginx restarting?"

while True:

    plan = controller.next(

        question

    )

    print(plan)

    if plan["completed"]:

        break

    fake_analysis = {

        "confidence": controller.state.confidence + 0.25

    }

    controller.feedback(

        plan["next"],

        fake_analysis,

    )

