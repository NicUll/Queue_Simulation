import unittest
from app.model import Model
from app.office import Office
from app.customer import Customer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.times = ("09:00", "18:00")
        self.time_per_customer = 2
        self.frequency = 0.2
        self.model = Model(self.times, self.time_per_customer, self.frequency)

    def test_office_creation(self):
        self.assertIsInstance(self.model.office, Office)
        self.assertEqual(self.model.office.time_per_customer, self.time_per_customer)
        self.assertEqual(self.model.office.open_time, self.times[0])
        self.assertEqual(self.model.office.close_time, self.times[1])
        self.assertEqual(self.model.next_out_time, None)

    def test_step(self):
        customer = None
        current_office_clock = self.model.office.clock
        steps = 0
        while customer is None:
            customer = self.model.step()
            steps += 1
        self.assertIsInstance(customer, Customer)
        self.assertEqual(self.model.office.clock, current_office_clock + steps)
        customer_errands = self.model.office.customers[0].errands
        next_out_time = customer_errands * self.model.office.time_per_customer
        self.assertEqual(next_out_time, self.model.next_out_time)

    def test_clock_conversion(self):
        self.assertEqual(self.model.current_timestring, "09:00")
        self.model.office.work()
        self.model.office.work()
        self.model.update_time()
        self.assertEqual(self.model.current_timestring, "09:02")
        for i in range(60):
            self.model.office.work()
        self.model.update_time()
        self.assertEqual(self.model.current_timestring, "10:02")

    def test_twenty_steps(self):
        self.model.update_time()
        print("Klockan är {} och postkontoret öppnar.".format(self.model.current_timestring))
        for i in range(20):
            new_customer = self.model.step()
            if new_customer is not None:
                print("Kl {} kommer kund {} in och...".format(self.model.current_timestring, new_customer.id))


if __name__ == '__main__':
    unittest.main()
