from remediation_engine.action import RemediationAction
from remediation_engine.policy import PolicyEngine

engine = PolicyEngine()

action = RemediationAction(

    action="patch_deployment",

    resource_type="Deployment",

    resource_name="payment-service",

    namespace="production",

    parameters={},

    confidence=0.96,

)

result = engine.evaluate(action)

print(result)
