from dataclasses import dataclass, field


@dataclass
class DryRunResult:

    success: bool

    preview: list = field(default_factory=list)

    warnings: list = field(default_factory=list)

    estimated_duration: str = ""

    expected_impact: str = ""

