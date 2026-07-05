class ResourceCache:

    def __init__(self):

        self.resources = {}

    def put(self, kind, data):

        self.resources[kind] = data

    def get(self, kind):

        return self.resources.get(kind, {})

    def all(self):

        return self.resources
