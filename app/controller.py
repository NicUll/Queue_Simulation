from tkinter import *


class Controller(Frame):

    HOURS = ["{:02d}".format(x) for x in range(24)]
    MINUTES = ["{:02d}".format(x) for x in range(60)]

    def __init__(self, root, simulation, model, savefile):
        """The controller in the form of sliders and buttons
        that controls the simulation and changes simulation parameters."""
        super(Controller, self).__init__(root)  # Used so that the controller is created properly by tkinter
        self.root = root
        self.simulation = simulation
        self.model = model
        self.savefile = savefile
        self.create_widgets()

    def create_widgets(self):
        """Method the create the controller objects"""
        self.start_button = Button(self, text="Starta", command=self.start)
        self.start_button.grid(row=0, column=0, columnspan=2,pady="5")
        self.reset_button = Button(self, text="Töm", command=self.reset)
        self.reset_button.grid(row=1, column=0, columnspan=2, pady="5")
        self.times = Label(self, text="Öppettider")
        self.times.grid(row=2,column=0,columnspan=2)
        self.save_button = Button(self, text="Spara", command=self.save)
        self.save_button.grid(row=5,column=0, columnspan=2)

        self.open_hour = StringVar(self.root)
        self.open_hour.set(self.savefile.open_times[0][:2])
        self.open_h_drop = OptionMenu(self, self.open_hour, *Controller.HOURS)

        self.open_minute = StringVar(self.root)
        self.open_minute.set(self.savefile.open_times[0][3:])
        self.open_m_drop = OptionMenu(self, self.open_minute, *Controller.MINUTES)

        self.close_hour = StringVar(self.root)
        self.close_hour.set(self.savefile.open_times[1][:2])
        self.close_h_drop = OptionMenu(self, self.close_hour, *Controller.HOURS)

        self.close_minute = StringVar(self.root)
        self.close_minute.set(self.savefile.open_times[1][3:])
        self.close_m_drop = OptionMenu(self, self.close_minute, *Controller.MINUTES)

        self.open_h_drop.grid(column=0, row=3)
        self.open_m_drop.grid(column=1, row=3)
        self.close_h_drop.grid(column=0, row=4)
        self.close_m_drop.grid(column=1, row=4)

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

    def save(self):
        open_time = self.open_hour.get() + ":" + self.open_minute.get()
        close_time = self.close_hour.get() + ":" + self.close_minute.get()
        self.model.office.open_time = open_time
        self.model.office.close_time = close_time

        self.savefile.save_data(self.model.office.time_per_customer, self.model.office.open_time, self.model.office.close_time,
                   self.model.new_customer_odds)
