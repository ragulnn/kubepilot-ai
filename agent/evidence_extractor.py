from datetime import datetime

from agent.evidence import Evidence


class EvidenceExtractor:

    def extract(self, tool, resources):

        evidence = []

        # -----------------------------
        # Pods
        # -----------------------------

        if tool == "pods":

            for pod in resources.get("pods", []):

                evidence.append(

                    Evidence(

                        type="pod",

                        resource=pod.get("name", ""),

                        namespace=pod.get(
                            "namespace",
                            "default",
                        ),

                        value=pod.get(
                            "status",
                            "Unknown",
                        ),

                        source_tool="pods",

                        timestamp=datetime.now().isoformat(),
                    )
                )

        # -----------------------------
        # Nodes
        # -----------------------------

        elif tool == "nodes":

            for node in resources.get("nodes", []):

                evidence.append(

                    Evidence(

                        type="node",

                        resource=node,

                        namespace="",

                        value="Ready",

                        source_tool="nodes",

                        timestamp=datetime.now().isoformat(),
                    )
                )

        # -----------------------------
        # Services
        # -----------------------------

        elif tool == "services":

            for svc in resources.get("services", []):

                evidence.append(

                    Evidence(

                        type="service",

                        resource=svc,

                        namespace="",

                        value="Found",

                        source_tool="services",

                        timestamp=datetime.now().isoformat(),
                    )
                )

        return evidence
