ACTION_RISK = {

    # ------------------------
    # Very Safe
    # ------------------------

    "rollout_restart": "LOW",

    "patch_deployment": "LOW",

    "patch_service": "LOW",

    # ------------------------
    # Medium
    # ------------------------

    "scale_deployment": "MEDIUM",

    "restart_pod": "MEDIUM",

    # ------------------------
    # High
    # ------------------------

    "drain_node": "HIGH",

    "cordon_node": "HIGH",

    "uncordon_node": "MEDIUM",

}
