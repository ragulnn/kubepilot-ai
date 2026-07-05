from learning_engine.repository import LearningRepository
from learning_engine.learner import InvestigationLearner


class LearningEngine:

    def __init__(self):

        self.repo = LearningRepository()

        self.learner = InvestigationLearner()

    def update(self):

        # ----------------------------------
        # Load Historical Incidents
        # ----------------------------------

        incidents = self.repo.load()

        # ----------------------------------
        # Learn Investigation Strategy
        # ----------------------------------

        learning = self.learner.learn(
            incidents
        )

        return learning
