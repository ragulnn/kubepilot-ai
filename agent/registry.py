from tools.pods import get_pods
from tools.logs import get_logs
from tools.describe import describe_pod
from tools.events import get_events
from tools.nodes import get_nodes
from tools.services import get_services
from tools.deployments import get_deployments
from tools.ingress import get_ingress
from tools.configmap import get_configmaps
from tools.secrets import get_secrets
from tools.namespaces import get_namespaces
from tools.pvc import get_pvc
from tools.pv import get_pv


TOOLS = {
    "pods": get_pods,
    "logs": get_logs,
    "describe": describe_pod,
    "events": get_events,
    "nodes": get_nodes,
    "services": get_services,
    "deployments": get_deployments,
    "ingress": get_ingress,
    "configmaps": get_configmaps,
    "secrets": get_secrets,
    "namespaces": get_namespaces,
    "pvc": get_pvc,
    "pv": get_pv,
}
