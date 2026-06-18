from utils.kubectl import run_kubectl


def get_pods():
    return run_kubectl("get pods -A")
