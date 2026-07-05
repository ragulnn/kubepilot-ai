from resolver.resource_index import ResourceIndex


class ResourceResolver:

    def __init__(self):

        self.index = ResourceIndex()

    def load(self, resources):

        for group in resources.values():

            if isinstance(group, list):

                for resource in group:

                    self.index.add(resource)

    def resolve(self, entity):

        return self.index.search(entity)
