from agent.validator import validate

print(validate("kubectl get pods"))              # True
print(validate("kubectl logs nginx"))            # True
print(validate("kubectl delete pod nginx"))      # False
print(validate("kubectl apply -f app.yaml"))     # False
print(validate("kubectl scale deployment nginx --replicas=5"))  # False
