import unittest
from app.eventhandler import EventHandler


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.eh1 = EventHandler()


    def test_string_method(self):
        self.expected_event = []
        self.eh1.time = "09:00"
        self.eh1.add_event("kund 3 kommer in", 0)
        self.expected_event.append("Kl 09:00 - kund 3 kommer in")
        self.eh1.add_event("kund 2 går", 1)
        self.eh1.add_event("kund 3 blir betjänad", 1)
        self.expected_event.append("Kl 09:00 - kund 2 går och kund 3 blir betjänad")
        iter = 0
        while(self.eh1.has_event):
            current_event = self.eh1.get_event()
            self.assertEqual(current_event, self.expected_event[iter])
            print(current_event)
            iter += 1
        print(self.eh1.get_event())




if __name__ == '__main__':
    unittest.main()
