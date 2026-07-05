import time
from datetime import datetime

from remediation_engine.handlers import KubernetesActionHandler
from remediation_engine.result import ExecutionResult


class KubernetesExecutor:

    def __init__(self):

        self.handler = KubernetesActionHandler()

    def execute(self, action):

        start = time.time()

        try:

            if action.action == "patch_deployment":

                response = self.handler.patch_deployment(

                    action

                )

            elif action.action == "rollout_restart":

                action.parameters[

                    "timestamp"

                ] = datetime.utcnow().isoformat()

                response = self.handler.rollout_restart(

                    action

                )

            elif action.action == "scale_deployment":

                response = self.handler.scale_deployment(

                    action

                )

            else:

                return ExecutionResult(

                    success=False,

                    action=action.action,

                    message="Unsupported action",

                )

            return ExecutionResult(

                success=True,

                action=action.action,

                message="Execution completed",

                resource_version=response.metadata.resource_version,

                execution_time=round(

                    time.time() - start,

                    3,

                ),

            )

        except Exception as e:

            return ExecutionResult(

                success=False,

                action=action.action,

                message=str(e),

                execution_time=round(

                    time.time() - start,

                    3,

                ),

            )
