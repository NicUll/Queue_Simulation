from random import random


class Customer(object):
    def __init__(self, in_time, id):
        """Create a new customer and generate the amount of errands they have
        and the time they entered the post-office."""

        self.in_time = in_time  # Time customer entered the office
        self.errands = Customer.generate_errands()  # Get a random amount of errands
        self.id = id  # Customers unique ID number

    @staticmethod
    def generate_errands():
        total_errands = 0
        while True:  # Loop through and add an errand with a 50% change of breaking
            total_errands += 1
            if random() < 0.5:
                break
        return total_errands
