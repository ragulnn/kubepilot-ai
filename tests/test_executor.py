from remediation_engine.action import RemediationAction
from remediation_engine.executor import KubernetesExecutor

executor = KubernetesExecutor()

action = RemediationAction(

    action="rollout_restart",

    resource_type="Deployment",

    resource_name="nginx",

    namespace="default",

    parameters={},

    reason="Restart deployment",

    confidence=0.95,

)

result = executor.execute(

    action

)

print(result)
