class FleetSummary:

    def summarize(

        self,

        health,

    ):

        print()

        print("=" * 60)

        print("Kubepilot Fleet Dashboard")

        print("=" * 60)

        print()

        print(

            f"Fleet Health Score : {health.score:.2f}"

        )

        print(

            f"Healthy Clusters   : {health.healthy_clusters}"

        )

        print(

            f"Unhealthy Clusters : {health.unhealthy_clusters}"

        )

        print(

            f"Total Clusters     : {health.total_clusters}"

        )

        print()

        if health.critical_clusters:

            print("Critical Clusters")

            print("-----------------------")

            for cluster in health.critical_clusters:

                print(

                    f"• {cluster}"

                )

        else:

            print(

                "No critical clusters."

            )
