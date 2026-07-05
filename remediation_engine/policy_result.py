from dataclasses import dataclass


@dataclass
class PolicyResult:

    allowed: bool

    requires_approval: bool

    message: str
