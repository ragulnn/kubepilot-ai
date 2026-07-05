"""
LLM Provider Package

Import every provider here so that each provider registers
itself automatically.
"""

from llm.providers.ollama import OllamaProvider

__all__ = [
    "OllamaProvider",
]
