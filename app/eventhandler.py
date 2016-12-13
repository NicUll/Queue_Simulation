from _collections import deque


class EventHandler(object):
    def __init__(self):
        self.time = ""
        self.events = deque([])
        self.has_event = False

    def clear_events(self):
        self.events = deque([])
        self.has_event = False

    def add_event(self, event, index):
        if index == len(self.events) - 1:
            self.events[index] += " och {}".format(event)
        else:
            self.events.append(event)
        self.has_event = True

    def get_event(self):
        if self.has_event:
            event = "Kl {} - {}".format(self.time, self.events.popleft())
            self.has_event = len(self.events) and True
            return event
        else:
            return "Inga nya händelser"

