from concurrent.futures import ThreadPoolExecutor, as_completed

from connectors.request import EvidenceRequest


class ParallelCollector:

    def __init__(self, registry):

        self.registry = registry

    def collect(self, requests: list[EvidenceRequest]):

        responses = []

        with ThreadPoolExecutor(
            max_workers=10
        ) as executor:

            futures = [

                executor.submit(
                    self.registry.collect,
                    request,
                )

                for request in requests

            ]

            for future in as_completed(
                futures
            ):

                responses.append(
                    future.result()
                )

        return responses
