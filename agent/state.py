from typing import TypedDict


class AgentState(TypedDict):
    question: str
    actions: list
    observations: list
    current_action: dict | None
    answer: str
    finished: bool
