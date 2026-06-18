from utils.kubectl import run_kubectl


def get_nodes():
    return run_kubectl("get nodes")
