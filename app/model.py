from app.office import Office
from app.eventhandler import EventHandler
from random import random


class Model(object):
    def __init__(self, times, time_per_customer, odds, x_size="800", y_size="640"):
        """Model object that holds the simulation parameters
        and an office and eventhandler object."""
        self.office = Office(times, time_per_customer)
        self.new_customer_odds = odds  # The odds of a customer entering the office
        self.event_handler = EventHandler()
        self.x_size = x_size  # Width of window
        self.y_size = y_size  # Height of window
        self.self_reset()  # Initialize additional object variables

    def self_reset(self):
        """Method used to reset only model-specific variables."""
        self.customers_in_queue = 0
        self.next_out_time = None
        self.current_timestring = self.office.open_time  # The current time in text format, e.g. 10:58

    def reset(self):
        """Method to reset the whole model and the objects it controls"""
        self.office.reset()
        self.event_handler.clear_events()
        self.self_reset()

    def step(self):
        """Method for stepping through the simulation one step
        i.e. one minute."""
        self.event_handler.time = self.current_timestring  # Update the event handlers time
        self.event_handler.clear_events()  # and erase previous events
        self.customers_in_queue = len(self.office.customers)  # Update que-length
        queue_not_empty_before = self.customers_in_queue and True  # Tells us wether we had customers before this minute

        # Block that handles generating new customers
        customer = None  # Create outside if-block for access further down
        # Generate a customer with a change of new_customer_odds e.g. 20% if it is 0.2
        if (random() < self.new_customer_odds) and self.office.open:
            customer = self.office.add_customer()
            self.event_handler.add_event(Office.office_events["new_customer"].format(customer.id))  # Add
            if queue_not_empty_before:
                self.event_handler.add_event(Office.office_events["customer_que"].format(self.customers_in_queue + 1),
                                             increase=False)

        # Block that handles finishing current customer
        if self.next_out_time == self.office.clock:  # Check if a customer should be done now and
            prev_customer = self.office.finish_customer()  # Remove them from the queue
            self.event_handler.add_event(Office.office_events["customer_leaves"].format(prev_customer.id))
            self.next_out_time = None

        # Block that handles getting to the next customer
        self.customers_in_queue = len(self.office.customers)  # Update length of queue
        # Check if no customer is being helped and there is a queue
        if self.next_out_time is None and self.customers_in_queue > 0:
            self.next_out_time = self.office.handle_customer()
            next_customer = self.office.customers[0]
            event_string = Office.office_events["customer_serviced_after_wait"].format(next_customer.id)
            if (next_customer == customer) and not queue_not_empty_before:
                event_string = Office.office_events["customer_serviced_immediately"]
            self.event_handler.add_event(event_string, increase=False)

        # Call work method on office and check if any events are returned

        if self.office.work() != 0:
            self.event_handler.add_event(self.office.office_events[self.office.latest_event])

        # Call method to generate the time-string for printing
        self.update_time()
        return customer

    def update_time(self):
        """Method for making the current time into a
        printable string for output"""
        start_hour = int(self.office.open_time[:2])
        start_minute = int(self.office.close_time[3:])
        current_office_clock = self.office.clock
        current_hour = start_hour + current_office_clock // 60
        current_minute = start_minute + current_office_clock % 60
        self.current_timestring = "{:02d}:{:02d}".format(current_hour, current_minute)
