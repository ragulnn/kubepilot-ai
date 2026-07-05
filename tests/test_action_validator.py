from remediation_engine.action import RemediationAction
from remediation_engine.validator import ActionValidator

validator = ActionValidator()

action = RemediationAction(

    action="patch_deployment",

    resource_type="Deployment",

    resource_name="payment-service",

    namespace="default",

    parameters={

        "memory_limit":"2Gi",

    },

    reason="Increase memory",

    confidence=0.96,

)

result = validator.validate(action)

print(result)
