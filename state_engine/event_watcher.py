from kubernetes import client, watch

from datetime import datetime

from state_engine.event import ClusterEvent


class ClusterEventWatcher:

    def __init__(self):

        self.core = client.CoreV1Api()

    def stream(self):

        watcher = watch.Watch()

        for event in watcher.stream(

            self.core.list_event_for_all_namespaces

        ):

            obj = event["object"]

            yield ClusterEvent(

                type=event["type"],

                resource=obj.involved_object.kind,

                namespace=obj.metadata.namespace,

                reason=obj.reason,

                message=obj.message,

                timestamp=datetime.utcnow().isoformat(),

            )
