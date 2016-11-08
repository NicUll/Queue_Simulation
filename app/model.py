from app.office import Office
from random import random


class Model(object):
    def __init__(self, times, time_per_customer, frequency):
        """Model object that holds the simulation parameters
        and an office object."""
        self.office = Office(times, time_per_customer)  # Create and store a post-office
        self.next_out_time = None  # Initialize a field that will keep track of current customers out time
        self.customers_in_queue = 0  # Total amount of customers that's been handled
        self.frequency = frequency  # The frequency with which customers enter the office
        self.current_timestring = times[0]  # The current time in text format, e.g. 10:58

    def step(self):
        """Method for stepping through the simulation one step
        i.e. one minute."""
        customer = None  # Generate a customer with a change of "frequency" e.g. 0.2
        if random() < self.frequency:
            customer = self.office.add_customer()
            print("Customer generated")
        if self.next_out_time == self.office.clock:  # Check if a customer should be done now and
            self.office.finish_customer()  # Remove them from the queue
            self.next_out_time = None
            print("Customer done")
        self.customers_in_queue = len(self.office.customers)
        if self.next_out_time is None and self.customers_in_queue > 0:
            # Check if no customer is being helped
            # and there is a queue
            self.next_out_time = self.office.handle_customer()
            print("Customer being handled")
        self.office.work()
        self.update_time()
        return customer

    def update_time(self):
        start_hour = int(self.office.open_time[:2])
        start_minute = int(self.office.close_time[3:])
        current_office_clock = self.office.clock
        current_hour = start_hour + current_office_clock // 60
        current_minute = start_minute + current_office_clock % 60
        self.current_timestring = "{:02d}:{:02d}".format(current_hour, current_minute)
