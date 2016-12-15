from _collections import deque


class EventHandler(object):
    def __init__(self):
        """Create a new eventhandler that adds new events to a deque-list
        together with the time they happened. Only holds one point in time
        but several events."""
        self.time = ""  # The time an event occurred, set from outside since an event might not know when it happened
        self.clear_events()

    def clear_events(self):
        """Method that resets the event-list, pointer and the boolean saying wether it has an event"""
        self.events = deque([])
        self.has_event = False
        self.current_index = 0

    def add_event(self, event, increase=True):
        """Add an event at the currently set time. The boolean
        increase determines wether the event happened at the same time
        as another (e.g. if time is in minutes, this would be the same second)."""
        if self.has_event:
            self.current_index += 1 * increase
            if (self.current_index == len(self.events) - 1) and (~increase):
                self.events[self.current_index] += " och {}".format(event)
                return
        else:
            self.has_event = True
        self.events.append(event)

    def get_event(self):
        """Method to collect the first event that happened at the latest time.
        The events are then removed (popped) and when no events are left
        has_event is set to False."""
        if self.has_event:
            event = "Kl {} - {}".format(self.time, self.events.popleft())
            self.has_event = len(self.events) and True
            return event
        else:  # Used if method is called even when handler has no events.
            return "Inga nya händelser"
