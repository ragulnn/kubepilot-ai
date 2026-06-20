from tools.describe import describe_pod
from tools.logs import get_logs
from tools.events import get_events


def troubleshoot_pod(pod_name, namespace="default"):

    report = ""

    report += "\n===== DESCRIPTION =====\n"
    report += describe_pod(pod_name, namespace)

    report += "\n===== LOGS =====\n"
    report += get_logs(pod_name, namespace)

    report += "\n===== EVENTS =====\n"
    report += get_events()

    return report
