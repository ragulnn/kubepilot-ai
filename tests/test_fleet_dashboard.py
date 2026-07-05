from fleet_engine.dashboard import FleetDashboard

from fleet_engine.summary import FleetSummary

fleet_result = {

    "clusters": 2,

    "healthy": 1,

    "issues": 1,

    "reports": [

        type(

            "Report",

            (),

            {

                "cluster": "kind",

                "root_cause": "Cluster healthy",

            },

        )(),

        type(

            "Report",

            (),

            {

                "cluster": "aks",

                "root_cause": "Cluster unavailable",

            },

        )(),

    ],

}

dashboard = FleetDashboard()

health = dashboard.build(

    fleet_result

)

FleetSummary().summarize(

    health

)
