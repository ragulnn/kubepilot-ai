from dataclasses import dataclass


@dataclass
class AIRequest:

    prompt: str

    schema: str = ""

    evidence: str = ""

    provider: str = "ollama"

    temperature: float = 0.0
