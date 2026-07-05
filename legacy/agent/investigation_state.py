class InvestigationState:

    def __init__(self):

        self.completed = set()

    def add(self, tool):

        self.completed.add(tool)

    def already_used(self, tool):

        return tool in self.completed

    def reset(self):

        self.completed.clear()
