from ollama import chat

from llm.provider import LLMProvider
from llm.registry import register_provider
from llm.response import LLMResponse


@register_provider
class OllamaProvider(LLMProvider):

    name = "ollama"

    def __init__(self):

        self.model = "qwen3:8b"

    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:

        response = chat(

            model=self.model,

            messages=[

                {

                    "role": "user",

                    "content": prompt,

                }

            ],

        )

        message = response["message"]["content"]

        return LLMResponse(

            success=True,

            content=message,

            provider=self.name,

            model=self.model,

            metadata=response,

        )
