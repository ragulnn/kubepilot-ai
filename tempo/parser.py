class TempoParser:

    def parse(self, data):

        if "batches" not in data:

            return []

        traces = []

        for batch in data["batches"]:

            resource = batch.get("resource", {})

            resource_attrs = {}

            for attr in resource.get("attributes", []):

                resource_attrs[attr["key"]] = attr["value"]

            for scope in batch.get("scopeSpans", []):

                for span in scope.get("spans", []):

                    traces.append(
                        {
                            "trace_id": span.get("traceId"),
                            "span_id": span.get("spanId"),
                            "parent_span_id": span.get("parentSpanId"),
                            "name": span.get("name"),
                            "kind": span.get("kind"),
                            "start_time": span.get("startTimeUnixNano"),
                            "end_time": span.get("endTimeUnixNano"),
                            "status": span.get("status", {}),
                            "service": resource_attrs.get("service.name", "unknown"),
                        }
                    )

        return traces
