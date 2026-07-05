class KnowledgeResolver:

    def resolve(self, incidents):

        if not incidents:

            return None

        return incidents[0]["incident"]
