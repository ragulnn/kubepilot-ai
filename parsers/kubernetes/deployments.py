from parsers.kubernetes.base import KubernetesParser


class DeploymentsParser(KubernetesParser):

    def parse(self, output):

        lines = output.strip().splitlines()

        if len(lines) <= 1:
            return []

        deployments = []

        for line in lines[1:]:

            parts = line.split()

            if len(parts) < 6:
                continue

            deployments.append({

                "kind": "Deployment",

                "namespace": parts[0],

                "name": parts[1],

                "ready": parts[2],

                "up_to_date": parts[3],

                "available": parts[4],

                "age": " ".join(parts[5:])

            })

        return deployments
