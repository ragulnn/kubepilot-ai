from workflow_engine.router import WorkflowRouter
from workflow_engine.executor import WorkflowExecutor

router = WorkflowRouter()

workflow = router.route(

    "Why is nginx crashing?"

)

responses = WorkflowExecutor().execute(

    workflow,

    "Why is nginx crashing?"

)

print()

print("Responses:", len(responses))

for r in responses:

    print()

    print(r.source)

    print(r.success)
