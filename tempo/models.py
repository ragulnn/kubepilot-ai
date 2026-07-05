from dataclasses import dataclass


@dataclass
class Trace:

    trace_id: str

    span_id: str

    parent_span_id: str | None

    name: str

    kind: str

    start_time: str

    end_time: str

    status: dict

    service: str
