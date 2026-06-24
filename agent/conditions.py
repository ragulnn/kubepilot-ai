def should_execute(state):
    """
    Decide what happens after the planner.

    Returns:
        execute
        analyze
    """

    action = state["current_action"]

    if action["tool"] == "finish":
        return "analyze"

    return "execute"
