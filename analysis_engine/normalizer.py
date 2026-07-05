from analysis_engine.evidence import Evidence


class EvidenceNormalizer:

    def normalize(self, responses):

        normalized = []

        for response in responses:

            source = getattr(
                response,
                "source",
                "unknown",
            )

            for item in getattr(
                response,
                "evidence",
                [],
            ):

                # --------------------------
                # Prometheus metrics
                # --------------------------

                if isinstance(item, dict):

                    for key, value in item.items():

                        normalized.append(

                            Evidence(

                                source=source,

                                category=source,

                                name=key,

                                value=value,

                            )

                        )

                # --------------------------
                # Loki logs
                # --------------------------

                elif isinstance(item, str):

                    normalized.append(

                        Evidence(

                            source=source,

                            category="logs",

                            name="logs",

                            value=item,

                        )

                    )

                # --------------------------
                # Tempo spans
                # --------------------------

                else:

                    normalized.append(

                        Evidence(

                            source=source,

                            category=source,

                            name=source,

                            value=item,

                        )

                    )

        return normalized
