from agents.pipeline import AgentPipeline

state = {
    "question": "Why is my nginx pod restarting?",
    "workflow": "pod",
}

pipeline = AgentPipeline()

result = pipeline.run(state)

print()
print("=" * 60)
print("Pipeline Result")
print("=" * 60)
print(result)
