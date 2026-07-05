from enum import Enum


class WorkflowType(str, Enum):

    POD = "pod_investigation"

    DEPLOYMENT = "deployment_investigation"

    SERVICE = "service_investigation"

    NETWORK = "network_investigation"

    STORAGE = "storage_investigation"

    NODE = "node_investigation"

    SECURITY = "security_investigation"

    GENERIC = "generic"
