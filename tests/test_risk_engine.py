from remediation_engine.action import RemediationAction
from remediation_engine.risk import RiskEngine

engine = RiskEngine()

action = RemediationAction(

    action="patch_deployment",

    resource_type="Deployment",

    resource_name="payment-service",

    namespace="default",

    parameters={},

    confidence=0.95,

)

result = engine.evaluate(

    action

)

print(result)
