from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.nodes import (
    planner_node,
    executor_node,
    analyzer_node,
)

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.add_node("analyzer", analyzer_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "executor")
workflow.add_edge("executor", "analyzer")
workflow.add_edge("analyzer", END)

graph = workflow.compile()
