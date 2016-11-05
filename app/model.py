from app.office import Office
from random import random


class Model(object):
    def __init__(self, times, time_per_customer, frequency):
        """Model object that holds the simulation parameters
        and an office object."""
        self.office = Office(times, time_per_customer)
        self.next_out_time = None
        self.customer_amount = 0
        self.frequency = frequency
        self.current_timestring = times[0]

    def step(self):
        customer = None
        if random() < self.frequency:
            customer = self.office.add_customer()
            self.customer_amount += 1
        if self.next_out_time is None and self.customer_amount > 0:
            self.next_out_time = self.office.handle_customer()
        #TODO check if a customer is done and go to next customer in queue
        #elif

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
