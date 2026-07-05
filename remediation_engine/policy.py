from remediation_engine.policy_registry import POLICIES
from remediation_engine.policy_result import PolicyResult


class PolicyEngine:

    def evaluate(self, action):

        namespace = action.namespace.lower()

        policy = POLICIES.get(namespace)

        if policy is None:

            return PolicyResult(

                allowed=False,

                requires_approval=True,

                message=f"No policy defined for namespace '{namespace}'",

            )

        if action.action not in policy["allow"]:

            return PolicyResult(

                allowed=False,

                requires_approval=True,

                message=f"Action '{action.action}' is not permitted in namespace '{namespace}'",

            )

        return PolicyResult(

            allowed=True,

            requires_approval=policy["approval_required"],

            message="Policy validation successful",

        )
