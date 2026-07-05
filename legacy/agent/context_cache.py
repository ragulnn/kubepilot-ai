import time


class ContextCache:

    def __init__(self):
        self.timestamp = 0
        self.data = None

    def valid(self):
        return (
            self.data is not None
            and time.time() - self.timestamp < 60
        )

    def get(self):
        return self.data

    def set(self, data):
        self.data = data
        self.timestamp = time.time()


cache = ContextCache()
