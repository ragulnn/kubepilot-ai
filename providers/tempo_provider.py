from providers.registry import register_tool

from tempo.client import TempoClient


@register_tool
class TempoProvider:

    name = "tempo"

    def __init__(self):

        self.client = TempoClient()

    def run(
        self,
        trace_id=None,
        limit=20,
    ):

        if trace_id:

            return self.client.trace(trace_id)

        return self.client.search(limit=limit)
