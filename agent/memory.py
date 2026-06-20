class Memory:

    def __init__(self):
        self.items = []

    def add(self, command, result):

        self.items.append({
            "command": command,
            "result": result
        })

    def all(self):
        return self.items

    def clear(self):
        self.items.clear()
