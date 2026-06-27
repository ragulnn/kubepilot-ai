from agent.workflow_engine import WorkflowEngine

engine = WorkflowEngine()

completed = []

print(engine.next_tool(
    "CrashLoopBackOff",
    completed
))

completed.append("logs")

print(engine.next_tool(
    "CrashLoopBackOff",
    completed
))

completed.append("describe")

print(engine.next_tool(
    "CrashLoopBackOff",
    completed
))

completed.append("events")

print(engine.next_tool(
    "CrashLoopBackOff",
    completed
))

