from typing import TypedDict, NotRequired


class Action(TypedDict):
    tool: str

    namespace: NotRequired[str]

    pod: NotRequired[str]

    deployment: NotRequired[str]

    service: NotRequired[str]

    node: NotRequired[str]

    ingress: NotRequired[str]

    configmap: NotRequired[str]

    secret: NotRequired[str]
