from dataclasses import dataclass
from typing import Optional


@dataclass
class Evidence:

    type: str

    resource: str

    namespace: str

    value: str

    confidence: float = 1.0

    source_tool: str = ""

    timestamp: Optional[str] = None
