import json
import uuid
from datetime import datetime
from pathlib import Path

from agent.similarity import SimilarityEngine


class Memory:

    def __init__(self):

        self.similarity = SimilarityEngine()

        self.memory_dir = Path("memory")

        self.memory_dir.mkdir(exist_ok=True)

    def save_incident(
        self,
        question,
        fingerprint,
        report,
        observations,
    ):

        incident = {
            "question": question,
            "fingerprint": fingerprint,
            "report": report,
            "observations": observations,
        }

        filename = (
            datetime.now().strftime("%Y%m%d_%H%M%S")
            + "_"
            + str(uuid.uuid4())[:8]
            + ".json"
        )

        filepath = self.memory_dir / filename

        with open(filepath, "w") as f:
            json.dump(
                incident,
                f,
                indent=4,
            )

        return filepath

    def load_all_incidents(self):

        incidents = []

        for file in sorted(
            self.memory_dir.glob("*.json")
        ):

            with open(file, "r") as f:

                incidents.append(
                    json.load(f)
                )

        return incidents

    def load_latest_incident(self):

        files = sorted(
            self.memory_dir.glob("*.json")
        )

        if not files:
            return None

        latest = files[-1]

        with open(latest, "r") as f:

            return json.load(f)

    def find_similar(
        self,
        fingerprint,
        top_k=5,
    ):

        results = []

        incidents = self.load_all_incidents()

        for incident in incidents:

            previous = incident["fingerprint"]

            score = self.similarity.compare(
                fingerprint,
                previous,
            )

            results.append(
                {
                    "score": score,
                    "incident": incident,
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True,
        )

        return results[:top_k]
