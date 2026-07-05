from dataclasses import dataclass, field


@dataclass
class Evidence:

    source: str

    category: str

    name: str

    value: object = None

    metadata: dict = field(default_factory=dict)
