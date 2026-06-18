from utils.kubectl import run_kubectl


def get_events():
    return run_kubectl("get events -A")
