import unittest
from app.office import Office
from app.customer import Customer
from _collections import deque


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.times = ("09:00", "18:00")
        self.time_per_customer = 2
        self.m_office = Office(self.times, self.time_per_customer)

    def test_creation(self):
        self.assertIsInstance(self.m_office, Office)
        self.assertEqual(self.m_office.time_per_customer, self.time_per_customer)
        self.assertEqual(self.m_office.open_time, self.times[0])
        self.assertEqual(self.m_office.close_time, self.times[1])
        self.assertEqual(self.m_office.clock, 0)
        self.assertEqual(self.m_office.customers, deque([]))

    def test_add_customer(self):
        customer1 = self.m_office.add_customer()
        self.assertIsInstance(customer1, Customer)  # Check that add_customer() returns a customer
        self.assertNotEqual(len(self.m_office.customers), 0) # Check that customer-list is not empty in office

    def test_work(self):
        current_clock = self.m_office.clock
        self.m_office.work()
        self.assertEqual(self.m_office.clock, current_clock + 1)

    def test_handle_customer(self):
        customer1 = self.m_office.add_customer()
        expected_out_time = self.time_per_customer * customer1.errands
        out_time = self.m_office.handle_customer()
        self.assertEqual(expected_out_time, out_time)

    def test_finish_customer(self):
        customer1 = self.m_office.add_customer()
        customer2 = self.m_office.add_customer()
        done_customer = self.m_office.finish_customer()
        self.assertEqual(self.m_office.customers, deque([customer2]))
        self.assertEqual(done_customer, customer1)
        done_customer = self.m_office.finish_customer()
        self.assertEqual(self.m_office.customers, deque([]))
        self.assertEqual(done_customer, customer2)


if __name__ == '__main__':
    unittest.main()
