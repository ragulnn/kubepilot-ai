from dataclasses import dataclass


@dataclass
class ExecutionResult:

    success: bool

    action: str

    message: str

    resource_version: str = ""

    execution_time: float = 0.0
