from capability_router.router import CapabilityRouter
from workflow_engine.workflow import Workflow


router = CapabilityRouter()

pod = Workflow(
    name="Pod",
    type="Pod",
    capabilities=[
        "logs",
        "describe",
        "events",
    ],
)

deployment = Workflow(
    name="Deployment",
    type="Deployment",
    capabilities=[
        "describe",
        "events",
    ],
)

service = Workflow(
    name="Service",
    type="Service",
    capabilities=[
        "describe",
        "events",
    ],
)

print(router.route(pod))
print(router.route(deployment))
print(router.route(service))
print(router.route(None))
