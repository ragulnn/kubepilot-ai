import tools
from tools.registry import TOOLS


class Executor:

    def execute(self, action: dict):

        if not isinstance(action, dict):
            raise Exception("Action must be a dictionary.")

        tool_name = action.get("tool")

        if tool_name == "finish":
            return "Investigation completed."

        if tool_name is None:
            raise Exception("Planner did not return a tool.")

        tool = TOOLS.get(tool_name)

        if tool is None:

            raise Exception(
                f"Tool '{tool_name}' not found.\n"
                f"Planner returned: {action}"
            )

        kwargs = action.copy()

        kwargs.pop("tool", None)

        kwargs = {
            k: v
            for k, v in kwargs.items()
            if v not in ("", None)
        }

        print(f"Running Tool : {tool_name}")

        if kwargs:
            print(f"Arguments    : {kwargs}")

        return tool.run(**kwargs)
