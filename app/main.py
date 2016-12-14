from app.view import View
from app.simulation import Simulation
from app.model import Model
from tkinter import *
from app.controller import Controller
from app.savefile import SaveFile

savefile = SaveFile("data.txt")
model = Model(savefile.open_times, savefile.time_per_customer, savefile.new_customer_odds)

root = Tk()
application = View(root, model)
application.grid(column=0, row=0)
simulation = Simulation(application, model, 5)

controller = Controller(root, simulation, model)
controller.grid(column=1, row=0)

application.simulation = simulation


def main():
    root.update()
    while model.office.is_working:
        if simulation.run:
            model.step()
            while model.event_handler.has_event:
                application.update_text_box("end", "\n" + model.event_handler.get_event())
        root.update()
    root.mainloop()


main()
