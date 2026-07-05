class ActionSimulator:

    def simulate(self, action):

        preview = []

        warnings = []

        duration = "Unknown"

        impact = "Unknown"

        # ---------------------------------

        if action.action == "patch_deployment":

            preview.append(

                f"Patch Deployment '{action.resource_name}'"

            )

            preview.append(

                f"Namespace: {action.namespace}"

            )

            preview.append(

                f"Parameters: {action.parameters}"

            )

            duration = "20-40 seconds"

            impact = "Rolling update"

        # ---------------------------------

        elif action.action == "rollout_restart":

            preview.append(

                f"Restart Deployment '{action.resource_name}'"

            )

            duration = "10-30 seconds"

            impact = "Pods will restart"

        # ---------------------------------

        elif action.action == "scale_deployment":

            preview.append(

                f"Scale '{action.resource_name}'"

            )

            duration = "5-20 seconds"

            impact = "Replica count changes"

        else:

            warnings.append(

                "Unknown execution impact."

            )

        return {

            "preview": preview,

            "warnings": warnings,

            "duration": duration,

            "impact": impact,

        }
