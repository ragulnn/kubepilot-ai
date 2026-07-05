from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.nodes import (
    planner_node,
    executor_node,
    analyzer_node,
)
from agent.conditions import should_execute
from agent.analyzer_conditions import investigation_complete


workflow = StateGraph(AgentState)

# -----------------------------
# Register Nodes
# -----------------------------

workflow.add_node("planner", planner_node)
workflow.add_node("executor", executor_node)
workflow.add_node("analyzer", analyzer_node)

# -----------------------------
# Entry Point
# -----------------------------

workflow.set_entry_point("planner")

# -----------------------------
# Planner
# -----------------------------
#
# Planner decides:
#   - execute another tool
#   - finish investigation
#

workflow.add_conditional_edges(
    "planner",
    should_execute,
    {
        "execute": "executor",
        END: END,
    },
)
# -----------------------------
# Executor
# -----------------------------
#
# Every executed tool is immediately analyzed.
#

workflow.add_edge(
    "executor",
    "analyzer",
)

# -----------------------------
# Analyzer
# -----------------------------
#
# Analyzer decides whether
# another investigation step
# is required.
#

workflow.add_conditional_edges(
    "analyzer",
    investigation_complete,
    {
        "continue": "planner",
        "finish": END,
    },
)

graph = workflow.compile()
