from app.office import Office
from random import random


class Model(object):
    def __init__(self, times, time_per_customer):
        """Model object that holds the simulation parameters
        and an office object."""
        self.office = Office(times, time_per_customer)

    def step(self):
        customer = None
        if random() < 0.2:
            customer = self.office.add_customer()
        self.office.work()
        return customer
