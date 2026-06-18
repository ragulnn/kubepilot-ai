from utils.kubectl import run_kubectl


def describe_pod(pod_name, namespace="default"):
    return run_kubectl(f"describe pod {pod_name} -n {namespace}")

