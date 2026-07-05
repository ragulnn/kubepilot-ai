class TempoSearchParser:

    def parse(self, data):

        traces = []

        for item in data.get("traces", []):

            traces.append({

                "trace_id": item.get("traceID"),

                "root_service": item.get("rootServiceName"),

                "root_trace": item.get("rootTraceName"),

                "start_time": item.get("startTimeUnixNano"),

            })

        return traces
