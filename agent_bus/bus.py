from collections import defaultdict


class AgentBus:

    def __init__(self):

        self._events = defaultdict(list)

    def publish(self, topic, value):

        self._events[topic].append(value)

    def get(self, topic):

        events = self._events.get(topic, [])

        if not events:
            return None

        return events[-1]

    def get_all(self, topic):

        return self._events.get(topic, [])

    def has(self, topic):

        return topic in self._events

    def clear(self):

        self._events.clear()

    def topics(self):

        return list(self._events.keys())
