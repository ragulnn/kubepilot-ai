POLICIES = {

    "dev": {

        "allow": [

            "patch_deployment",
            "rollout_restart",
            "restart_pod",
            "scale_deployment",

        ],

        "approval_required": False,

    },

    "staging": {

        "allow": [

            "patch_deployment",
            "rollout_restart",
            "restart_pod",
            "scale_deployment",

        ],

        "approval_required": True,

    },

    "production": {

        "allow": [

            "patch_deployment",
            "rollout_restart",

        ],

        "approval_required": True,

    },

}
