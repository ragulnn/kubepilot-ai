from dataclasses import dataclass


@dataclass
class RollbackResult:

    success: bool

    message: str

    restored_version: str = ""

    duration: float = 0.0
