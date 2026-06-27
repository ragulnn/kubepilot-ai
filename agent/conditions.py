from langgraph.graph import END


def should_execute(state):
    """
    Decide what happens after the planner.

    Returns:
        "execute" -> Execute a Kubernetes tool
        END       -> Finish the investigation
    """

    action = state.get("current_action")

    if action is None:
        return END

    tool = action.get("tool")

    if tool == "finish":
        return END

    return "execute"
