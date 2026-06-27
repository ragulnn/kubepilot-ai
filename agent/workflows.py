WORKFLOWS = {

    "CrashLoopBackOff": [
        "logs",
        "describe",
        "events"
    ],

    "ImagePullBackOff": [
        "describe",
        "events"
    ],

    "Pending": [
        "events",
        "nodes"
    ],

    "OOMKilled": [
        "describe"
    ]
}
