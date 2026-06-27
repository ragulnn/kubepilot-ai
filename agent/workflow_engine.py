from agent.workflows import WORKFLOWS


class WorkflowEngine:

    def next_tool(self, issue, completed):

        if issue not in WORKFLOWS:
            return None

        workflow = WORKFLOWS[issue]

        for tool in workflow:

            if tool not in completed:
                return tool

        return "finish"
