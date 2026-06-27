from enum import Enum


class AgentStatus(str, Enum):

    ONLINE = "online"

    OFFLINE = "offline"

    DEGRADED = "degraded"

    STARTING = "starting"
