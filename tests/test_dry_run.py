from remediation_engine.action import RemediationAction
from remediation_engine.dry_run import DryRunEngine

engine = DryRunEngine()

action = RemediationAction(

    action="patch_deployment",

    resource_type="Deployment",

    resource_name="payment-service",

    namespace="default",

    parameters={

        "memory_limit":"2Gi"

    },

    reason="Increase memory",

    confidence=0.96,

)

result = engine.execute(

    action

)

print(result)
