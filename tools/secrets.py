from utils.kubectl import run_kubectl


def get_secrets():
    return run_kubectl("get secrets -A")
