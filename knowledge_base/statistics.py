class IncidentStatistics:

    def summarize(self, incidents):

        summary = {}

        for incident in incidents:

            root = incident["incident"]["root_cause"]

            summary.setdefault(root, 0)

            summary[root] += 1

        return summary
