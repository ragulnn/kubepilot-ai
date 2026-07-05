from abc import ABC, abstractmethod

from llm.response import LLMResponse


class LLMProvider(ABC):

    name = ""

    @abstractmethod
    def generate(

        self,

        prompt: str,

    ) -> LLMResponse:

        pass
