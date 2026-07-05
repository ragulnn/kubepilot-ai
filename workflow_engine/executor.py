from expansion_engine.automatic_expander import AutomaticExpander
from evidence_engine.dispatcher import EvidenceDispatcher
from resource_engine.discovery import ResourceDiscovery


class WorkflowExecutor:

    def __init__(self):

        self.discovery = ResourceDiscovery()

        self.expander = AutomaticExpander()

        self.dispatcher = EvidenceDispatcher()

    def execute(self, workflow, question):

        resources = self.discovery.discover(question)

        if not resources:

            return []

        workflow.target = resources[0]["name"]

        workflow.namespace = resources[0]["namespace"]

        requests = self.expander.expand(workflow)

        responses = self.dispatcher.collect(requests)

        return responses
