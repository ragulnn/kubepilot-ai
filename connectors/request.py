from dataclasses import dataclass, field


@dataclass
class EvidenceRequest:
    """
    Generic evidence request used by every connector and
    every Kubepilot Agent.
    """

    # ---------- Routing ----------

    cluster: str = "default"

    # ---------- Evidence ----------

    type: str = ""

    # ---------- Resource ----------

    resource: str | None = None

    resource_type: str | None = None

    namespace: str | None = None

    labels: dict = field(default_factory=dict)

    annotations: dict = field(default_factory=dict)

    keyword: str | None = None

    # ---------- Metrics ----------

    metric: str | None = None

    # ---------- Logs ----------

    log_level: str | None = None

    # ---------- Time ----------

    since: str | None = None

    time_range: str = "5m"

    # ---------- Filters ----------

    filters: dict = field(default_factory=dict)

    # ---------- Limits ----------

    limit: int = 100

    # ---------- Investigation ----------

    include_events: bool = False

    include_logs: bool = False

    include_metrics: bool = False

    include_traces: bool = False
