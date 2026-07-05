from datetime import datetime

from state_engine.collector import ClusterCollector
from state_engine.state import ClusterState


class ClusterWatcher:

    def __init__(self):

        self.collector = ClusterCollector()

    def snapshot(self):

        state = ClusterState(

            timestamp=datetime.utcnow().isoformat()

        )

        # -------------------------------

        for pod in self.collector.pods():

            state.pods[pod.metadata.name] = {

                "namespace": pod.metadata.namespace,

                "phase": pod.status.phase,

            }

        # -------------------------------

        for deploy in self.collector.deployments():

            state.deployments[deploy.metadata.name] = {

                "namespace": deploy.metadata.namespace,

                "replicas": deploy.status.ready_replicas,

            }

        # -------------------------------

        for svc in self.collector.services():

            state.services[svc.metadata.name] = {

                "namespace": svc.metadata.namespace,

                "type": svc.spec.type,

            }

        # -------------------------------

        for node in self.collector.nodes():

            state.nodes[node.metadata.name] = {

                "ready": True,

            }

        # -------------------------------

        for event in self.collector.events():

            state.events.append({

                "reason": event.reason,

                "message": event.message,

            })

        return state
