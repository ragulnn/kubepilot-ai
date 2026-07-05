from memory.repository import IncidentRepository
from memory.similarity import SimilarityEngine


class IncidentSearch:

    def __init__(self):

        self.repo = IncidentRepository()

        self.engine = SimilarityEngine()

    def find(self, incident):

        matches = []

        for old in self.repo.load():

            score = self.engine.score(

                incident,

                old,

            )

            matches.append(

                {

                    "score": score,

                    "incident": old,

                }

            )

        matches.sort(

            key=lambda x: x["score"],

            reverse=True,

        )

        return matches[:5]
