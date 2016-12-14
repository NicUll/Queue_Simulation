from _collections import deque


class EventHandler(object):
    def __init__(self):
        self.time = ""
        self.clear_events()

    def clear_events(self):
        self.events = deque([])
        self.has_event = False
        self.current_index = 0

    def add_event(self, event, increase=True):
        if self.has_event:
            self.current_index += 1 * increase
            if (self.current_index == len(self.events) - 1) and (~increase):
                self.events[self.current_index] += " och {}".format(event)
            else:
                self.events.append(event)
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
