from abc import ABC, abstractmethod


class KubernetesTool(ABC):

    name = ""
    description = ""

    @abstractmethod
    def run(self, **kwargs):
        pass
