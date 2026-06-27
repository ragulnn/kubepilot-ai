from dataclasses import dataclass, field


@dataclass
class EvidenceResponse:
    """
    Standard response returned by every connector.
    """

    source: str

    success: bool

    evidence: list = field(default_factory=list)

    message: str = ""
