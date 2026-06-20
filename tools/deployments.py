from utils.kubectl import run_kubectl


def get_deployments():
    return run_kubectl("get deployments -A")
