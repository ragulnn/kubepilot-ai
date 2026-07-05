import time
import requests

from loki.parser import LokiParser


class LokiClient:

    def __init__(self):

        self.url = "http://localhost:3100"

        self.parser = LokiParser()

    # -----------------------------------------
    # Instant Query
    # -----------------------------------------

    def query(
        self,
        query,
        limit=100,
    ):

        response = requests.get(
            f"{self.url}/loki/api/v1/query",
            params={
                "query": query,
                "limit": limit,
            },
            timeout=20,
        )

        response.raise_for_status()

        return self.parser.parse(
            response.json()
        )

    # -----------------------------------------
    # Range Query
    # -----------------------------------------

    def query_range(
        self,
        query,
        minutes=10,
        limit=200,
    ):

        end = int(time.time() * 1e9)

        start = end - (minutes * 60 * 1000000000)

        response = requests.get(

            f"{self.url}/loki/api/v1/query_range",

            params={

                "query": query,

                "start": start,

                "end": end,

                "limit": limit,

                "direction": "backward",

            },

            timeout=20,

        )

        response.raise_for_status()

        return self.parser.parse(
            response.json()
        )
