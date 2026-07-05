from remediation_engine.simulator import ActionSimulator
from remediation_engine.dry_result import DryRunResult


class DryRunEngine:

    def __init__(self):

        self.simulator = ActionSimulator()

    def execute(self, action):

        result = self.simulator.simulate(

            action

        )

        return DryRunResult(

            success=True,

            preview=result["preview"],

            warnings=result["warnings"],

            estimated_duration=result["duration"],

            expected_impact=result["impact"],

        )
