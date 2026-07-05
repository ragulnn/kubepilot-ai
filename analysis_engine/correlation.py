from analysis_engine.evidence import Evidence


class CorrelationEngine:

    def correlate(self, evidence):

        correlated = []

        memory = None
        restarts = None
        logs = []
        traces = []

        for item in evidence:

            if item.name == "memory":
                memory = item.value

            elif item.name == "restarts":
                restarts = item.value

            elif item.name == "logs":
                logs.append(item.value)

            elif item.name == "traces":
                traces.append(item.value)

        correlated.extend(evidence)

        if (
            memory is not None
            and memory >= 0.95
            and restarts is not None
            and restarts > 5
        ):

            correlated.append(

                Evidence(

                    source="correlation",

                    category="correlation",

                    name="memory_restart",

                    value=True,

                )

            )

        if logs and traces:

            correlated.append(

                Evidence(

                    source="correlation",

                    category="correlation",

                    name="logs_traces",

                    value=True,

                )

            )

        return correlated
