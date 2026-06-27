from connectors.parallel import ParallelCollector
from connectors.default_registry import registry
from connectors.request import EvidenceRequest

collector = ParallelCollector(registry)

requests = [

    EvidenceRequest(type="pods"),

    EvidenceRequest(type="services"),

    EvidenceRequest(type="nodes"),

]

responses = collector.collect(requests)

for response in responses:

    print("=" * 50)

    print(response.source)

    print(response.success)

    print(len(response.evidence))
