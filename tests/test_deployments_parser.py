from utils.kubectl import run_kubectl
from parsers.kubernetes.deployments import DeploymentsParser

output = run_kubectl(
    "get deployments -A"
)

deployments = DeploymentsParser().parse(output)

print(deployments)
