class SnapshotManager:

    def create(self, resource):

        return {

            "resource": resource,

            "version": "previous",

        }

    def restore(self, snapshot):

        return True
