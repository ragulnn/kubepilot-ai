from kubernetes import config

from state_engine.event_watcher import ClusterEventWatcher

config.load_kube_config()

watcher = ClusterEventWatcher()

for event in watcher.stream():

    print(event)
