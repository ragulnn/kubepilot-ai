from agent.tool_schema import TOOL_SCHEMAS


class Validator:

    def validate(self, action):

        tool = action.get("tool")

        if tool not in TOOL_SCHEMAS:
            return False, f"Unknown tool: {tool}"

        required_fields = TOOL_SCHEMAS[tool]

        missing = []

        for field in required_fields:
            if field not in action:
                missing.append(field)

        if missing:
            return False, f"Missing fields: {', '.join(missing)}"

        return True, None
