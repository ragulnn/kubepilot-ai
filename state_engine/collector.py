from kubernetes import client


class ClusterCollector:

    def __init__(self):

        self.core = client.CoreV1Api()
        self.apps = client.AppsV1Api()

    # -------------------------------------

    def pods(self):

        return self.core.list_pod_for_all_namespaces().items

    # -------------------------------------

    def deployments(self):

        return self.apps.list_deployment_for_all_namespaces().items

    # -------------------------------------

    def services(self):

        return self.core.list_service_for_all_namespaces().items

    # -------------------------------------

    def nodes(self):

        return self.core.list_node().items

    # -------------------------------------

    def events(self):

        return self.core.list_event_for_all_namespaces().items
