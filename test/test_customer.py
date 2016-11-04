import unittest
from app.customer import Customer


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.m_office_clock = 0
        self.m_cust1 = Customer(self.m_office_clock)
        self.m_cust1_in_time = 0

    def test_creation(self):
        self.assertIsInstance(self.m_cust1, Customer)

    def test_in_time(self):
        in_time = self.m_cust1.in_time
        self.assertEqual(in_time, self.m_cust1_in_time)
        print("\nTime in minutes from opening time: {}".format(in_time), end="")

    def test_errand_amount_generator(self):
        errands = self.m_cust1.errands
        self.assertGreaterEqual(errands, 1)
        print("\nAmount of errands: {}".format(errands), end="")


if __name__ == '__main__':
    unittest.main()
