from expansion_engine.expander import ExpansionEngine
from evidence_engine.dispatcher import EvidenceDispatcher
from connectors.request import EvidenceRequest


class ExpansionPipeline:

    def __init__(self):

        self.expander = ExpansionEngine()
        self.dispatcher = EvidenceDispatcher()

    def collect(self, resource):

        expanded = self.expander.expand(resource)

        requests = []

        for item in expanded:

            requests.append(

                EvidenceRequest(

                    type=item["type"],

                    kind=resource.get("kind"),

                    name=resource.get("name"),

                    namespace=resource.get(
                        "namespace",
                        "default",
                    ),

                )

            )

        print()

        print("Expansion Requests")

        for request in requests:

            print(request)

        print()

        return self.dispatcher.collect(requests)
