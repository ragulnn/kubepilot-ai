import providers
from providers.registry import TOOLS

tool = TOOLS["metrics"]

result = tool.run(
    name="nginx-7f8fbb96d-pt7cq",
    metric="cpu",
)

print(result)
