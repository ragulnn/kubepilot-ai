from parsers.kubernetes.base import KubernetesParser


class NodesParser(KubernetesParser):

    def parse(self, output):

        lines = output.strip().splitlines()

        if len(lines) <= 1:
            return []

        nodes = []

        for line in lines[1:]:

            parts = line.split()

            if len(parts) < 5:
                continue

            nodes.append({

                "kind": "Node",

                "name": parts[0],

                "status": parts[1],

                "roles": parts[2],

                "age": parts[3],

                "version": parts[4],

            })

        return nodes
