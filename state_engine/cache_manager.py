from state_engine.resource_cache import ResourceCache


class CacheManager:

    def __init__(self):

        self.cache = ResourceCache()

    def update(self, state):

        self.cache.put("pods", state.pods)

        self.cache.put("deployments", state.deployments)

        self.cache.put("services", state.services)

        self.cache.put("nodes", state.nodes)

        self.cache.put("events", state.events)

    def get(self, resource):

        return self.cache.get(resource)

    def snapshot(self):

        return self.cache.all()
