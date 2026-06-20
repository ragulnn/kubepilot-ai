from tools.registry import TOOLS


class Executor:

    def execute(self, action: dict):

        tool_name = action["tool"]

        tool = TOOLS.get(tool_name)

        if tool is None:
            raise Exception(f"Tool '{tool_name}' not found.")

        kwargs = action.copy()
        kwargs.pop("tool")

        return tool.run(**kwargs)
