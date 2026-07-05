from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class Evidence:

    source: str

    type: str

    resource: str = ""

    namespace: str = ""

    status: str = ""

    timestamp: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    data: Any = None

