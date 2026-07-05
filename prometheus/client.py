import requests


class PrometheusClient:

    def __init__(self, url="http://localhost:9090"):

        self.url = url.rstrip("/")

    def query(self, promql):

        endpoint = f"{self.url}/api/v1/query"

        response = requests.get(

            endpoint,

            params={

                "query": promql,

            },

            timeout=10,

        )

        response.raise_for_status()

        return response.json()
