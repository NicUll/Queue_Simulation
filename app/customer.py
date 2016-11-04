from random import random


class Customer(object):
    def __init__(self, in_time):
        """Create a new customer and generate the amount of errands they have
        and the time they entered the post-office."""

        self.in_time = in_time
        self.errands = Customer.generate_errands()

    @staticmethod
    def generate_errands():
        total_errands = 0
        while True:
            total_errands += 1
            if random() < 0.5:
                break
        return total_errands
