from app.office import Office
from app.eventhandler import EventHandler
from random import random


class Model(object):
    def __init__(self, times, time_per_customer, frequency, x_size="800", y_size="640"):
        """Model object that holds the simulation parameters
        and an office object."""
        self.office = Office(times, time_per_customer)  # Create and store a post-office
        self.next_out_time = None  # Initialize a field that will keep track of current customers out time
        self.customers_in_queue = 0  # Total amount of customers that's been handled
        self.frequency = frequency  # The frequency with which customers enter the office
        self.current_timestring = times[0]  # The current time in text format, e.g. 10:58
        self.x_size = x_size
        self.y_size = y_size
        self.event_handler = EventHandler()

    def step(self):
        """Method for stepping through the simulation one step
        i.e. one minute."""

        self.event_handler.time = self.current_timestring  # Update the event handlers
        self.event_handler.clear_events()  # time and erase prev events

        # Block that handles generating new customers
        customer = None  # Generate a customer with a change of "frequency" e.g. 0.2
        if (random() < self.frequency) and self.office.open:
            customer = self.office.add_customer()
            self.event_handler.add_event("Kund {} kommer in".format(customer.id))

        # Block that handles finishing current customer
        queue_empty_before = True
        if self.next_out_time == self.office.clock:  # Check if a customer should be done now and
            self.event_handler.add_event("får plats {} i kön".format(len(self.office.customers)), increase=False)
            prev_customer = self.office.finish_customer()  # Remove them from the queue
            self.event_handler.add_event("Kund {} går".format(prev_customer.id))
            self.next_out_time = None
            queue_empty_before = False

        # Block that handles getting to the next customer
        self.customers_in_queue = len(self.office.customers)
        # Check if no customer is being helped and there is a queue
        if self.next_out_time is None and self.customers_in_queue > 0:
            self.next_out_time = self.office.handle_customer()
            next_customer = self.office.customers[0]
            event_string = "kund {} blir betjänad".format(next_customer.id)
            if (next_customer == customer) and queue_empty_before:
                event_string = "blir genast betjänad"
            self.event_handler.add_event(event_string, increase=False)

        # Call work method on office and check if any events are returned
        if self.office.work() > 0:
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
