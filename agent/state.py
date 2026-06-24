from typing import TypedDict


class AgentState(TypedDict):
    question: str
    current_action: dict | None
    observations: list
    answer: str
    finished: bool
