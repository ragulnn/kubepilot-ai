from utils.kubectl import run_kubectl


def get_logs(pod_name, namespace="default"):
    return run_kubectl(f"logs -n {namespace} {pod_name}")
