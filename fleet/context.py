from kubernetes import config


class ClusterContext:

    def switch(

        self,

        cluster,

    ):

        config.load_kube_config(

            context=cluster.context

        )

        return cluster.context
