from workflow_engine.workflow import Workflow
from workflow_engine.types import WorkflowType

from agents.pipeline import AgentPipeline

print("=" * 60)
print("Kubepilot Full Pipeline")
print("=" * 60)

pipeline = AgentPipeline()

workflow = Workflow(

    name=WorkflowType.POD,

    namespace="default",

)

state = {

    "question": input("Question: "),

    "workflow": workflow,

}

result = pipeline.run(state)

print()

print("=" * 60)
print("Pipeline Finished")
print("=" * 60)

print()

print(result.get("report_text", "No report generated"))
