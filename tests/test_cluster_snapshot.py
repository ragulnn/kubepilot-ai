from kubernetes import config

from state_engine.manager import StateManager

config.load_kube_config()

manager = StateManager()

state = manager.refresh()

print(state)

print()

print(state.pods.keys())

print(state.deployments.keys())

print(state.nodes.keys())
