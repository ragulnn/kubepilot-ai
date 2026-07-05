from dataclasses import dataclass


@dataclass
class RemediationRequest:

    analysis: dict

    verification: dict

    memory: list

    knowledge: dict
