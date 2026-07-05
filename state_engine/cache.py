class StateCache:

    def __init__(self):

        self.state = None

    def update(self, state):

        self.state = state

    def get(self):

        return self.state

    def clear(self):

        self.state = None
