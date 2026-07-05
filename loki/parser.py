class LokiParser:

    def parse(self, response):

        results = []

        data = response.get("data", {})

        streams = data.get("result", [])

        for stream in streams:

            labels = stream.get("stream", {})

            values = stream.get("values", [])

            for ts, log in values:

                results.append(

                    {

                        "labels": labels,

                        "timestamp": ts,

                        "log": log,

                    }

                )

        return results
