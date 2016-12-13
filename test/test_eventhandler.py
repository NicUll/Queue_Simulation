import unittest
from app.eventhandler import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.eh1 = EventHandler()

    def test_string_method(self):
        self.eh1.time = "09:00"
        self.eh1.add_event("kommer kund 1 in")
        self.assertEqual("Kl 09:00 kommer kund 1 in", str(self.eh1))
        print(self.eh1)

    def test_add_event(self):
        self.eh1.time = "09:00"
        self.eh1.add_event("kommer kund 1 in")
        self.eh1.add_event("kund 2 går")
        self.assertEqual("Kl 09:00 kommer kund 1 in och kund 2 går", str(self.eh1))
        print(self.eh1)
        self.eh1.add_event("kund 3 står bara där")
        self.assertEqual("Kl 09:00 kommer kund 1 in, kund 2 går och kund 3 står bara där", str(self.eh1))
        print(self.eh1)

    def test_clear_events(self):
        self.assertFalse(self.eh1.has_event)
        self.eh1.time = "09:00"
        self.eh1.add_event("kommer kund 1 in")
        self.assertEqual("Kl 09:00 kommer kund 1 in", str(self.eh1))
        self.assertTrue(self.eh1.has_event)
        print(self.eh1)
        self.eh1.clear_events()
        self.assertFalse(self.eh1.has_event)
        self.eh1.add_event("kommer 23 kunder in")
        self.assertEqual("Kl 09:00 kommer 23 kunder in", str(self.eh1))


if __name__ == '__main__':
    unittest.main()
