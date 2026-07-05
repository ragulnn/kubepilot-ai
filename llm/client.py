import llm.providers

from llm.registry import PROVIDERS


class LLMClient:

    def __init__(

        self,

        provider="ollama",

    ):

        if provider not in PROVIDERS:

            raise Exception(

                f"Unknown provider: {provider}"

            )

        self.provider = PROVIDERS[provider]

    def generate(

        self,

        prompt,

    ):

        return self.provider.generate(

            prompt

        )
