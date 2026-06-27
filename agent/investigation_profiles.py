from connectors.request import EvidenceRequest


class InvestigationProfiles:

    @staticmethod
    def fast():

        return [

            EvidenceRequest(type="pods"),

            EvidenceRequest(type="events"),

        ]

    @staticmethod
    def standard():

        return [

            EvidenceRequest(type="pods"),

            EvidenceRequest(type="events"),

            EvidenceRequest(type="logs"),

        ]

    @staticmethod
    def deep():

        return [

            EvidenceRequest(type="pods"),

            EvidenceRequest(type="events"),

            EvidenceRequest(type="logs"),

            EvidenceRequest(type="deployments"),

            EvidenceRequest(type="services"),

            EvidenceRequest(type="nodes"),

            EvidenceRequest(type="configmap"),

            EvidenceRequest(type="secret"),

            EvidenceRequest(type="pv"),

            EvidenceRequest(type="pvc"),

            EvidenceRequest(type="ingress"),

        ]
