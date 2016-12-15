from app.view import View
from app.simulation import Simulation
from app.model import Model
from tkinter import *
from app.controller import Controller
from app.savefile import SaveFile


savefile = SaveFile("data.txt")  # Collect simulation parameters
model = Model(savefile.open_times, savefile.time_per_customer, savefile.new_customer_odds)  # Create model

root = Tk()  # Create the TK window
view = View(root, model)  # Generate output window
view.grid(column=0, row=0)  # Place window to the left

simulation = Simulation(view, model, 5)  # Make the object that controls all events

controller = Controller(root, simulation, model, savefile)  # Create the GUI to interact with the simulation
controller.grid(column=1, row=0, sticky=(N,S))  # Place controllers to the right


def task():  # Function that runs all the time
    simulation.run_simulation()
    root.update_idletasks()
    root.update()
    root.after(0, task)


root.update()
root.after(0, task)
root.mainloop()

