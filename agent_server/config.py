import os


class Config:

    CLUSTER_NAME = os.getenv(
        "CLUSTER_NAME",
        "default",
    )

    SERVER_PORT = int(
        os.getenv(
            "SERVER_PORT",
            8080,
        )
    )

    AUTH_TOKEN = os.getenv(
        "AUTH_TOKEN",
        "kubepilot",
    )
