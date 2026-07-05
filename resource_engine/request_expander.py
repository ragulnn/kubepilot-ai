class RequestExpander:

    def expand(self, pods):

        requests = []

        for pod in pods:

            requests.append({

                "type": "describe",

                "resource": pod["name"],

                "namespace": pod["namespace"],

            })

            requests.append({

                "type": "logs",

                "pod": pod["name"],

                "namespace": pod["namespace"],

            })

        requests.append({

            "type": "events",

            "namespace": "default",

        })

        return requests
