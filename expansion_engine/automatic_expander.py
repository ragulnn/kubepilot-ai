from connectors.request import EvidenceRequest
from workflow_engine.types import WorkflowType

class AutomaticExpander:

    def expand(self, workflow):

        requests = []

        if workflow.name == WorkflowType.POD:

            requests.append(
                EvidenceRequest(
                    type="describe",
                    kind="Pod",
                    name=workflow.target,
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="logs",
                    kind="Pod",
                    name=workflow.target,
                    namespace=workflow.namespace,
                )
            )

            requests.append( 
                EvidenceRequest(
                     type="events",
                     kind="Pod",
                     name=workflow.target,
                     namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="traces",
                    kind="Pod",
                    name=workflow.target,
                    namespace=workflow.namespace,
               )
           )
        elif workflow.name == WorkflowType.DEPLOYMENT:

            requests.append(
                EvidenceRequest(
                    type="deployments",
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="events",
                    namespace=workflow.namespace,
                )
            )

        elif workflow.name == WorkflowType.SERVICE:

            requests.append(
                EvidenceRequest(
                    type="services",
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="events",
                    namespace=workflow.namespace,
                )
            )

        elif workflow.name == WorkflowType.NETWORK:

            requests.append(
                EvidenceRequest(
                    type="ingress",
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="services",
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="events",
                    namespace=workflow.namespace,
                )
            )

        elif workflow.name == WorkflowType.STORAGE:

            requests.append(
                EvidenceRequest(
                    type="pvc",
                    namespace=workflow.namespace,
                )
            )

            requests.append(
                EvidenceRequest(
                    type="pv",
                )
            )

        elif workflow.name == WorkflowType.NODE:

            requests.append(
                EvidenceRequest(
                    type="nodes",
                )
            )

        return requests
