from utils.kubectl import run_kubectl
from parsers.kubernetes.pods import PodsParser

output = run_kubectl("get pods -A")

pods = PodsParser().parse(output)

print()

print("Pods Found:", len(pods))

print()

print(pods[0])
