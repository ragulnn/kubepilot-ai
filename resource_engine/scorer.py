from difflib import SequenceMatcher


class ResourceScorer:

    def score(
        self,
        query: str,
        resource_name: str,
    ) -> int:

        query = query.lower().strip()
        resource = resource_name.lower().strip()

        # Exact match
        if query == resource:
            return 100

        # Prefix match
        if resource.startswith(query):
            return 95

        # Contains
        if query in resource:
            return 90

        # Similarity
        similarity = SequenceMatcher(
            None,
            query,
            resource,
        ).ratio()

        return int(similarity * 100)
