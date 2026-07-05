class InvestigationMode:

    INFO = "information"

    DIAGNOSTIC = "diagnostic"

    HEALTH = "health"

    def detect(self, question: str):

        q = question.lower()

        # Health checks

        if any(word in q for word in [
            "health",
            "healthy",
            "status",
            "cluster",
            "overall",
        ]):
            return self.HEALTH

        # Diagnostic questions

        if any(word in q for word in [
            "why",
            "error",
            "crash",
            "failing",
            "failed",
            "pending",
            "restart",
            "issue",
            "problem",
            "debug",
            "diagnose",
            "not working",
        ]):
            return self.DIAGNOSTIC

        # Everything else is information gathering

        return self.INFO
