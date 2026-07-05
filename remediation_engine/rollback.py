import time

from remediation_engine.snapshot import SnapshotManager
from remediation_engine.rollback_result import RollbackResult


class RollbackEngine:

    def __init__(self):

        self.snapshot = SnapshotManager()

    def rollback(

        self,

        resource,

    ):

        start = time.time()

        snapshot = self.snapshot.create(

            resource

        )

        restored = self.snapshot.restore(

            snapshot

        )

        if restored:

            return RollbackResult(

                success=True,

                message="Rollback completed successfully.",

                restored_version=snapshot["version"],

                duration=round(

                    time.time() - start,

                    3,

                ),

            )

        return RollbackResult(

            success=False,

            message="Rollback failed.",

            duration=round(

                time.time() - start,

                3,

            ),

        )
