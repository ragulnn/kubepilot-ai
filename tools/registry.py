TOOLS = {}


def register_tool(cls):
    tool = cls()
    TOOLS[tool.name] = tool
    return cls
