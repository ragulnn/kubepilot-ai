from dataclasses import dataclass


@dataclass
class TraceSearchResult:

    trace_id: str

    root_service: str | None = None

    root_span: str | None = None
