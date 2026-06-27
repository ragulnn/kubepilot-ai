from enum import Enum


class EvidenceType(str, Enum):

    PODS = "pods"

    DEPLOYMENTS = "deployments"

    SERVICES = "services"

    EVENTS = "events"

    LOGS = "logs"

    METRICS = "metrics"

    TRACES = "traces"

    NODES = "nodes"

    PVC = "pvc"

    PV = "pv"

    CONFIGMAP = "configmap"

    SECRET = "secret"

    INGRESS = "ingress"
