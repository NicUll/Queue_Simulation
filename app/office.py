from app.customer import Customer
from _collections import deque


class Office(object):
    def __init__(self, times, time_per_customer):
        """Create a post-office object with parameters for
        business-hours and the time it takes per customer.
        A list is also initiated that will hold the customer queue,
        together with an index keeping track of current customer."""
        self.open_time = times[0]  # The time the office opens
        self.close_time = times[1]  # The time the office closes
        self.time_per_customer = time_per_customer  # Time it takes to handle a customer
        self.clock = 0  # Current clock time in minutes, increments every time customer is handled
        self.customers = deque([])  # A deque (list) holding current customers in que
        self.total_customer_amount = 0  # Total customers that has entered the office up until now
        self.open = True
        # Todo make use of self.open and close the office when appropriate

    def add_customer(self):
        """Add a customer to the queue.
        Return the customer object"""
        self.total_customer_amount += 1  # Increment total amount of customers that has come
        new_customer = Customer(self.clock, self.total_customer_amount)  # Create new customer (ID = total amount)
        self.customers.append(new_customer)  # Add customers to que-list
        return new_customer

    def handle_customer(self):
        """Start helping customer, return end-time"""
        current_customer = self.customers[0]  # Select first customer in the queue
        out_time = current_customer.errands * self.time_per_customer  # Time customer will leave
        return out_time

    def work(self):
        self.clock += 1  # Increment office clock by one

    def finish_customer(self):
        """Increase the customer queue index
        i.e. go to next customer."""
        return self.customers.popleft()  # Remove customer from queue when done
