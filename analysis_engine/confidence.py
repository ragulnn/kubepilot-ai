from models.specialist_result import SpecialistResult


class ConfidenceTracker:

    def __init__(self):

        self.confidence = 0.0

    def update(self, specialist):

        if specialist is None:

            return self.confidence

        if isinstance(specialist, SpecialistResult):

            c = specialist.confidence

        elif isinstance(specialist, dict):

            c = specialist.get(

                "confidence",

                0.0,

            )

        else:

            c = 0.0

        if c > self.confidence:

            self.confidence = c

        return self.confidence
