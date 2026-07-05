class InvestigationStrategy:

    REQUIRED_EVIDENCE = {

        "Application Crash": [
            "pod",
            "log",
            "event",
        ],

        "Container Image Missing": [
            "pod",
            "event",
        ],

        "Scheduling Problem": [
            "pod",
            "node",
            "event",
        ],

        "Node Failure": [
            "node",
            "event",
        ],

        "Unknown": [
            "pod",
        ],
    }

    def missing(self, root_cause, evidence_store):

        required = self.REQUIRED_EVIDENCE.get(

            root_cause,

            self.REQUIRED_EVIDENCE["Unknown"],

        )

        existing = {

            e.type

            for e in evidence_store.all()

        }

        return [

            item

            for item in required

            if item not in existing

        ]

