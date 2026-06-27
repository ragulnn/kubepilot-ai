class QuestionClassifier:

    SIMPLE_COMMANDS = [
        "show",
        "list",
        "get",
        "display"
    ]

    INVESTIGATION_KEYWORDS = [
        "why",
        "error",
        "issue",
        "problem",
        "crash",
        "crashing",
        "restart",
        "restarting",
        "failed",
        "failure",
        "diagnose",
        "investigate",
        "analyze"
    ]

    def classify(self, question):

        q = question.lower()

        for word in self.INVESTIGATION_KEYWORDS:
            if word in q:
                return "investigation"

        for word in self.SIMPLE_COMMANDS:
            if q.startswith(word):
                return "simple"

        return "investigation"


