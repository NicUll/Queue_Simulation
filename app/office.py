from app.customer import Customer
from _collections import deque


class Office(object):
    def __init__(self, times, time_per_customer):
        """Create a post-office object with parameters for
        business-hours and the time it takes per customer.
        A list is also initiated that will hold the customer queue,
        together with an index keeping track of current customer."""
        self.open_time = times[0]
        self.close_time = times[1]
        self.time_per_customer = time_per_customer
        self.clock = 0
        self.customers = deque([])
        self.total_customer_amount = 0

    def add_customer(self):
        """Add a customer to the queue.
        Return the customer object"""
        self.total_customer_amount += 1
        new_customer = Customer(self.clock, self.total_customer_amount)
        self.customers.append(new_customer)
        return new_customer

    def handle_customer(self):
        """Start helping customer, return end-time"""
        current_customer = self.customers[0]
        out_time = current_customer.errands * self.time_per_customer
        return out_time

    def work(self):
        self.clock += 1

    def finish_customer(self):
        """Increase the customer queue index
        i.e. go to next customer."""
        return self.customers.popleft()
