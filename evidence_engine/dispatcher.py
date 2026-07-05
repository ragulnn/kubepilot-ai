from concurrent.futures import ThreadPoolExecutor

from connectors.request import EvidenceRequest
from evidence_engine.collector import EvidenceCollector


class EvidenceDispatcher:

    def __init__(self):

        self.collector = EvidenceCollector()

    def _collect_one(
        self,
        request: EvidenceRequest,
    ):

        print(
            f"Collecting {request.type}"
        )

        return self.collector.collect(
            request
        )

    def collect(
        self,
        requests: list[EvidenceRequest],
    ):

        if not requests:
            return []

        with ThreadPoolExecutor(
            max_workers=min(8, len(requests))
        ) as executor:

            results = list(

                executor.map(

                    self._collect_one,

                    requests,

                )

            )

        return results
