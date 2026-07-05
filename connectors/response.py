from dataclasses import dataclass, field

from connectors.request import EvidenceRequest


@dataclass
class EvidenceResponse:
    """
    Standard response returned by every connector.
    """

    # Original request that produced this response
    request: EvidenceRequest | None = None

    # Connector name
    source: str = ""

    # Whether collection succeeded
    success: bool = False

    # Collected evidence
    evidence: list = field(default_factory=list)

    # Human-readable message
    message: str = ""

    # Optional metadata
    latency: float = 0.0

    metadata: dict = field(default_factory=dict)
