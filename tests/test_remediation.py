from agent.remediation import Remediation

r = Remediation()

print(r.recommend("CrashLoopBackOff"))
print(r.recommend("OOMKilled"))

