from datetime import datetime

from state_engine.state import ClusterState
from state_engine.cache import StateCache
from state_engine.watcher import ClusterWatcher
from kubernetes import config

class StateManager:

    def __init__(self):
         config.load_kube_config()
         self.cache = StateCache()
         self.watcher = ClusterWatcher()

    def refresh(self):

           state = self.watcher.snapshot()

           self.cache.update(state)

           return state
    def current(self):

        return self.cache.get()
