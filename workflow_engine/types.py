from enum import Enum


class WorkflowType(str, Enum):

    POD = "pod"

    DEPLOYMENT = "deployment"

    SERVICE = "service"

    NETWORK = "network"

    STORAGE = "storage"

    NODE = "node"

    SECURITY = "security"

    GENERIC = "generic"
