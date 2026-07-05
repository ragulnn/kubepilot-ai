import requests

from tempo.parser import TempoParser
from tempo.search_parser import TempoSearchParser


class TempoClient:

    def __init__(self):

        self.url = "http://localhost:3200"

        self.parser = TempoParser()

        self.search_parser = TempoSearchParser()

    def trace(
        self,
        trace_id,
    ):

        response = requests.get(
            f"{self.url}/api/traces/{trace_id}",
            timeout=20,
        )

        response.raise_for_status()

        return self.parser.parse(
            response.json()
        )

    def search(
        self,
        limit=20,
    ):

        response = requests.get(
            f"{self.url}/api/search",
            params={
                "limit": limit,
            },
            timeout=20,
        )

        response.raise_for_status()

        return self.search_parser.parse(
            response.json()
        )
