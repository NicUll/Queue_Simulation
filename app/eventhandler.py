

class EventHandler(object):
    def __init__(self):
        self.time = ""
        self.events = []
        self.has_event = False

    def clear_events(self):
        self.events = []
        self.has_event = False

    def add_event(self, event):
        self.events.append(event)
        self.has_event = True

    def __str__(self):
        if self.has_event:

            event_string = self.events[0]
            for i in range(1, len(self.events) - 1):
                event_string += ", " + self.events[i]
            if len(self.events) > 1:
                event_string += " och " + self.events[-1]
            return "Kl {} {}".format(self.time, event_string)
        else:
            return "Inga händelser"
