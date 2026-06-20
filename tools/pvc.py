from utils.kubectl import run_kubectl


def get_pvc():
    return run_kubectl("get pvc -A")
