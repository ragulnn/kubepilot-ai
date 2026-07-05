import json
import os


class LearningRepository:

    def __init__(self):

        self.path = "learning_engine/history.json"

    def load(self):

        if not os.path.exists(self.path):
            return []

        with open(self.path) as f:

            try:
                return json.load(f)
            except Exception:
                return []

    def save(self, item):

        history = self.load()

        history.append(item)

        with open(self.path, "w") as f:

            json.dump(history, f, indent=4)
