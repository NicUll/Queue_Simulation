from tkinter import *


class Controller(Frame):
    def __init__(self, master, simulation, model):
        """The controller in the form of sliders and buttons
        that changes simulation parameters."""
        super(Controller, self).__init__(master)
        self.master = master
        self.simulation = simulation
        self.model = model
        self.start_button = Button(self, text="Starta", command=self.start)
        self.start_button.grid(row=0, column=0)
        self.reset_button = Button(self, text="Återställ", command=self.reset)
        self.reset_button.grid(row=1, column=0)

    def start(self):
        self.simulation.start_simulation()

    def reset(self):
        self.simulation.view.reset()
        self.model.reset()
