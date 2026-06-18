from utils.kubectl import run_kubectl


def get_services():
    return run_kubectl("get svc -A")
