import unittest
from app.view import View
from app.model import Model
from app.simulation import Simulation
from tkinter import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.times = ("09:00", "18:00")
        self.time_per_customer = 2
        self.frequency = 0.2
        self.model = Model(self.times, self.time_per_customer, self.frequency)


        self.root = Tk()
        self.application = View(self.root, self.model)
        self.simulation = Simulation(self.application, self.model, 5)
        self.application.simulation = self.simulation

    def test_something(self):
        self.root.update()
        while self.model.office.is_working:
            if self.simulation.run:
                self.model.step()
                while self.model.event_handler.has_event:
                    self.application.update_text_box("end", "\n" + self.model.event_handler.get_event())

            self.root.update()
        self.root.mainloop()


if __name__ == '__main__':
    unittest.main()

