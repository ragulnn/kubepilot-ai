from dataclasses import dataclass


@dataclass
class AgentRegistration:

    cluster: str

    hostname: str

    ip: str

    version: str

    token: str
