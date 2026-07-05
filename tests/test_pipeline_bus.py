from agents.pipeline import AgentPipeline

pipeline = AgentPipeline()

state = {

    "question": "Why is nginx crashing?"

}

pipeline.run(state)

print()

print("Bus Topics")

print(pipeline.bus.topics())

print()

print("Workflow")

print(pipeline.bus.get("workflow"))
