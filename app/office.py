from app.customer import Customer
from _collections import deque


class Office(object):
    office_events = {0: "Inga händelser",
                     "new_customer": "Kund {} kommer in",
                     "customer_que": "får plats {} i kön",
                     "customer_leaves": "Kund {} går",
                     "customer_serviced_after_wait": "kund {} blir betjänad",
                     "customer_serviced_immediately": "blir genast betjänad",
                     "close_doors": "Kontoret stänger dörrarna",
                     "office_closed": "Kontoret har stängt helt för dagen",
                     "office_robbed": "Kontoret har blivit rånat"}

    def __init__(self, times, time_per_customer):
        """Create a post-office object with parameters for
        business-hours and the time it takes per customer.
        A list is also initiated that will hold the customer queue,
        together with an index keeping track of current customer."""
        self.open_time = times[0]  # The time the office opens
        self.close_time = times[1]  # The time the office closes
        self.time_per_customer = time_per_customer  # Time it takes to handle a customer
        self.reset()

    def reset(self):
        self.clock = 0  # Current clock time in minutes, increments every time customer is handled
        self.customers = deque([])  # A deque (list) holding current customers in que
        self.total_customer_amount = 0  # Total customers that has entered the office up until now
        self.open = True
        self.is_working = True
        self.latest_event = 0
        self.total_wait_time = 0
        self.total_work_time = 0
        self.open_time_in_minutes = self.calculate_open_time()

    def calculate_open_time(self):
        open_in_minutes = Office.clock_to_minutes(self.open_time)
        close_in_minutes = Office.clock_to_minutes(self.close_time)
        return close_in_minutes - open_in_minutes

    @staticmethod
    def clock_to_minutes(time):
        hours = int(time[:2])
        minutes = int(time[3:])
        return hours * 60 + minutes

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
        self.total_wait_time += (self.clock - current_customer.in_time)
        self.total_work_time += current_customer.errands * self.time_per_customer
        out_time = self.clock + current_customer.errands * self.time_per_customer  # Time customer will leave
        return out_time

    def work(self):
        self.clock += 1  # Increment office clock by one
        self.latest_event = 0
        if not self.open and (len(self.customers) == 0):
            self.is_working = False
            self.latest_event = "office_closed"
        if self.clock == self.open_time_in_minutes:
            self.open = False
            self.latest_event = "close_doors"

        return self.latest_event

    def finish_customer(self):
        """Increase the customer queue index
        i.e. go to next customer."""
        return_customer = self.customers.popleft()  # Remove customer from queue when done

        return return_customer
