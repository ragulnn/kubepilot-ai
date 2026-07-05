from agents.pipeline import AgentPipeline

pipeline = AgentPipeline()

state = {
    "question": "Why is nginx crashing?"
}

result = pipeline.run(state)

print()
print("Pipeline Finished")
print(result)
