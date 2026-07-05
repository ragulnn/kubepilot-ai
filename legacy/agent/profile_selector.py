from agent.investigation_profiles import InvestigationProfiles


class ProfileSelector:

    def choose(self, question: str):

        question = question.lower()

        if any(word in question for word in [

            "why",

            "root cause",

            "crash",

            "failed",

            "error",

            "issue",

            "problem",

        ]):

            return InvestigationProfiles.deep()

        if any(word in question for word in [

            "status",

            "show",

            "list",

            "get",

        ]):

            return InvestigationProfiles.fast()

        return InvestigationProfiles.standard()
