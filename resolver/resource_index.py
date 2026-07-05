class ResourceIndex:

    def __init__(self):

        self.resources = []

    def add(self, resource):

        self.resources.append(resource)

    def search(self, keyword):

        keyword = keyword.lower()

        matches = []

        for resource in self.resources:

            name = resource.get("name", "").lower()

            if keyword in name:

                matches.append(resource)

        return matches
