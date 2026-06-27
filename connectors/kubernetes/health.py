from utils.kubectl import run_kubectl


def cluster_healthy():

    try:

        run_kubectl("cluster-info")

        return True

    except Exception:

        return False
