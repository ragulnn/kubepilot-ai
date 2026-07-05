from parsers.kubernetes.base import KubernetesParser


class PodsParser(KubernetesParser):

    def parse(self, output):

        lines = output.strip().splitlines()

        if len(lines) <= 1:
            return []

        pods = []

        for line in lines[1:]:

            parts = line.split()

            if len(parts) < 6:
                continue

            namespace = parts[0]
            name = parts[1]
            ready = parts[2]
            status = parts[3]

            try:
                restarts = int(parts[4])
            except Exception:
                restarts = parts[4]

            age = " ".join(parts[5:])

            pods.append({

                "kind": "Pod",

                "namespace": namespace,

                "name": name,

                "ready": ready,

                "status": status,

                "restarts": restarts,

                "age": age,

            })

        return pods
