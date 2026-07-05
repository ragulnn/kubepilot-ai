class PrometheusParser:

    def parse(self, response, metric):

        if not response:
            return None

        if response.get("status") != "success":
            return None

        results = response.get("data", {}).get("result", [])

        if not results:
            return {
                "source": "prometheus",
                "metric": metric,
                "value": None,
                "unit": "",
                "labels": {},
            }

        sample = results[0]

        labels = sample.get("metric", {})

        value = sample.get("value", [])

        if len(value) >= 2:
            timestamp = value[0]

            try:
                metric_value = float(value[1])
            except Exception:
                metric_value = None
        else:
            timestamp = None
            metric_value = None

        return {

            "source": "prometheus",

            "metric": metric,

            "value": metric_value,

            "timestamp": timestamp,

            "labels": labels,

        }
