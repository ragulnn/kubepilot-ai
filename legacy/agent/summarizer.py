class Summarizer:

    def summarize(self, tool, raw_output):

        summary = {
            "tool": tool
        }

        if tool == "pods":

            lines = raw_output.splitlines()

            running = 0
            pending = 0
            failed = 0
            crashloop = 0

            for line in lines:

                if "CrashLoopBackOff" in line:
                    crashloop += 1

                elif "Running" in line:
                    running += 1

                elif "Pending" in line:
                    pending += 1

                elif "Error" in line:
                    failed += 1

            summary.update({
                "running": running,
                "pending": pending,
                "failed": failed,
                "crashloop": crashloop,
                "total": len(lines)
            })

        else:

            summary["preview"] = "\n".join(
                raw_output.splitlines()[:10]
            )

        return summary

    def summarize_history(self, observations):

        history = []

        for i, obs in enumerate(observations, start=1):

            history.append(
                f"""
Step {i}

Tool:
{obs["tool"]}

Summary:
{obs["summary"]}
"""
            )

        return "\n".join(history)

    def collect_resources(self, observations):

        resources = {
            "pods": [],
            "deployments": [],
            "nodes": [],
            "services": [],
        }

        for obs in observations:

            extracted = obs.get(
                "resources",
                {}
            )

            for key in resources:

                resources[key].extend(
                    extracted.get(
                        key,
                        []
                    )
                )

        return resources
