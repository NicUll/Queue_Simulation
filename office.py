class Office(object):
    def __init__(self, times, time_per_customer):
        """Create a post-office object with parameters for
        business-hours and the time it takes per customer.
        A list is also initiated that will hold the customer queue,
        together with an index keeping track of current customer."""
        pass

    def add_customer(self, customer):
        """Add a customer to the queue.
        Return their place in the queue"""
        pass

    def customer_done(self, out_time):
        """Increase the customer queue index
        i.e. go to next customer."""
        pass
