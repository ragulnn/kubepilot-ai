from kubernetes import client


class KubernetesActionHandler:

    def __init__(self):

        self.apps = client.AppsV1Api()

        self.core = client.CoreV1Api()

    # ------------------------------------------------

    def patch_deployment(self, action):

        body = {

            "spec": {

                "template": {

                    "spec": {

                        "containers": [

                            {

                                "name": action.resource_name,

                                "resources": {

                                    "limits": {

                                        "memory": action.parameters.get(
                                            "memory_limit",
                                            "512Mi",
                                        )
                                    }
                                }

                            }

                        ]

                    }

                }

            }

        }

        return self.apps.patch_namespaced_deployment(

            name=action.resource_name,

            namespace=action.namespace,

            body=body,

        )

    # ------------------------------------------------

    def rollout_restart(self, action):

        body = {

            "spec": {

                "template": {

                    "metadata": {

                        "annotations": {

                            "kubectl.kubernetes.io/restartedAt": "__NOW__"

                        }

                    }

                }

            }

        }

        return self.apps.patch_namespaced_deployment(

            name=action.resource_name,

            namespace=action.namespace,

            body=body,

        )

    # ------------------------------------------------

    def scale_deployment(self, action):

        replicas = action.parameters.get(

            "replicas",

            1,

        )

        body = {

            "spec": {

                "replicas": replicas

            }

        }

        return self.apps.patch_namespaced_deployment_scale(

            name=action.resource_name,

            namespace=action.namespace,

            body=body,

        )
