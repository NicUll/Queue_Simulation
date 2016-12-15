from tkinter import *


class Controller(Frame):
    def __init__(self, root, simulation, model):
        """The controller in the form of sliders and buttons
        that controls the simulation and changes simulation parameters."""
        super(Controller, self).__init__(root)  # Used so that the controller is created properly by tkinter
        self.root = root
        self.simulation = simulation
        self.model = model
        self.create_widgets()

    def create_widgets(self):
        """Method the create the controller objects"""
        self.start_button = Button(self, text="Starta", command=self.start)
        self.start_button.grid(row=0, column=0)
        self.reset_button = Button(self, text="Återställ", command=self.reset)
        self.reset_button.grid(row=1, column=0)

    def start(self):
        """Method called when clicking the start button"""
        self.simulation.start_simulation()
        self.start_button["state"] = "disabled"  # Make start button un-clickable

    def reset(self):
        """Method called when clicking the reset button"""
        self.simulation.pause_simulation()
        # Call methods to reset simulation and model to normal state,
        # model in turn calls reset on office
        self.simulation.view.reset()
        self.model.reset()
        self.start_button["state"] = "normal"  # Make start button clickable
