from knowledge_base.statistics import IncidentStatistics
from knowledge_base.ranking import IncidentRanking
from knowledge_base.resolver import KnowledgeResolver


class KnowledgeEngine:

    def __init__(self):

        self.statistics = IncidentStatistics()

        self.ranking = IncidentRanking()

        self.resolver = KnowledgeResolver()

    def build(self, incidents):

        ranked = self.ranking.rank(

            incidents

        )

        best = self.resolver.resolve(

            ranked

        )

        stats = self.statistics.summarize(

            ranked

        )

        return {

            "best_match": best,

            "statistics": stats,

            "total_incidents": len(ranked),

        }
