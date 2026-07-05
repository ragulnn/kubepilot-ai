class EventDispatcher:

    def __init__(self):

        self.handlers = []

    def register(self, handler):

        self.handlers.append(handler)

    def dispatch(self, event):

        for handler in self.handlers:

            handler(event)
