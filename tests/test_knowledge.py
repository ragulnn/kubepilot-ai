from agent.knowledge import KnowledgeEngine

engine = KnowledgeEngine()

print(engine.next_step("CrashLoopBackOff"))
print(engine.next_step("Pending"))
print(engine.next_step("OOMKilled"))
