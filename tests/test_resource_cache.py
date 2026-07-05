from kubernetes import config

from state_engine.manager import StateManager
from state_engine.cache_manager import CacheManager

config.load_kube_config()

state = StateManager().refresh()

cache = CacheManager()

cache.update(state)

print(cache.snapshot().keys())

print()

print(cache.get("pods"))
