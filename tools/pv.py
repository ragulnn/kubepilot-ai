from utils.kubectl import run_kubectl


def get_pv():
    return run_kubectl("get pv")
