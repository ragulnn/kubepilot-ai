from utils.kubectl import run_kubectl


def get_ingress():
    return run_kubectl("get ingress -A")
