import unittest
from app.model import Model
from app.office import Office
from app.customer import Customer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.times = ("09:00", "18:00")
        self.time_per_customer = 2
        self.model = Model(self.times, self.time_per_customer)

    def test_office_creation(self):
        self.assertIsInstance(self.model.office, Office)
        self.assertEqual(self.model.office.time_per_customer, self.time_per_customer)
        self.assertEqual(self.model.office.times, self.times)

    def test_step(self):
        customer = None
        current_office_clock = self.model.office.clock
        steps = 0
        while customer is None:
            customer = self.model.step()
            steps += 1
        self.assertIsInstance(customer, Customer)
        self.assertEqual(self.model.office.clock, current_office_clock + steps)


if __name__ == '__main__':
    unittest.main()
