from parsers.kubernetes.base import KubernetesParser


class ServicesParser(KubernetesParser):

    def parse(self, output):

        lines = output.strip().splitlines()

        if len(lines) <= 1:
            return []

        services = []

        for line in lines[1:]:

            parts = line.split()

            if len(parts) < 5:
                continue

            services.append({

                "kind": "Service",

                "namespace": parts[0],

                "name": parts[1],

                "type": parts[2],

                "cluster_ip": parts[3],

                "ports": parts[4],

            })

        return services
