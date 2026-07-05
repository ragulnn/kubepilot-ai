class InvestigationStatistics:

    def summarize(self, history):

        stats = {}

        for incident in history:

            for action in incident.get("actions", []):

                stats[action] = stats.get(action, 0) + 1

        return stats
