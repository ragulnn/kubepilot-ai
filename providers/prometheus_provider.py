from prometheus.parser import PrometheusParser
from providers.base import KubernetesTool
from providers.registry import register_tool

from prometheus.client import PrometheusClient
from prometheus import queries


@register_tool
class PrometheusMetricsTool(KubernetesTool):

    name = "metrics"

    description = "Collect Prometheus metrics"

    def __init__(self):

        self.client = PrometheusClient()
        self.parser = PrometheusParser()

    def run(self, **kwargs):

        pod = kwargs.get("name")

        metric = kwargs.get(
            "metric",
            "cpu",
        )

        if not pod:

            raise Exception(
                "MetricsTool requires a pod name."
            )

        if metric == "cpu":

            promql = queries.CPU_USAGE.format(
                pod=pod,
            )

        elif metric == "memory":

            promql = queries.MEMORY_USAGE.format(
                pod=pod,
            )

        elif metric == "restarts":

            promql = queries.RESTART_COUNT.format(
                pod=pod,
            )

        elif metric == "ready":

            promql = queries.READY_STATUS.format(
                pod=pod,
            )

        elif metric == "phase":

            promql = queries.POD_PHASE.format(
                pod=pod,
            )

        elif metric == "network_rx":

            promql = queries.NETWORK_RX.format(
                pod=pod,
            )

        elif metric == "network_tx":

            promql = queries.NETWORK_TX.format(
                pod=pod,
            )

        else:

            raise Exception(
                f"Unknown metric: {metric}"
            )

        response = self.client.query(promql)

        return self.parser.parse(
            response,
            metric,
        )
