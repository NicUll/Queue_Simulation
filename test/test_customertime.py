import unittest
from app.customertime import CustomerTime


class MyTestCase(unittest.TestCase):

    def setUp(self):
        CustomerTime.set_open_time("07:00")
        self.time1 = CustomerTime("08:00")

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
