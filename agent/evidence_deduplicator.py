from agent.evidence import Evidence


class EvidenceDeduplicator:

    def exists(self, store, evidence: Evidence):

        for item in store.all():

            if (
                item.type == evidence.type
                and item.resource == evidence.resource
                and item.namespace == evidence.namespace
                and item.value == evidence.value
            ):
                return True

        return False
