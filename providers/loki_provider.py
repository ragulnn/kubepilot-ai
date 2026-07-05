from providers.registry import register_tool

from loki.client import LokiClient
from loki import queries


@register_tool
class LokiProvider:

    name = "loki"

    def __init__(self):

        self.client = LokiClient()

    def run(

        self,

        resource=None,

        name=None,

        namespace="default",

    ):

        # -------------------------------------
        # Pod logs
        # -------------------------------------

        if name:

            query = queries.POD_LOGS % (

                namespace,

                name,

            )

        # -------------------------------------
        # Namespace logs
        # -------------------------------------

        else:

            query = queries.NAMESPACE_LOGS % (

                namespace,

            )

        return self.client.query_range(

            query=query,

            minutes=10,

        )
