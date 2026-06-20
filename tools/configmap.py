from utils.kubectl import run_kubectl


def get_configmaps():
    return run_kubectl("get configmaps -A")
