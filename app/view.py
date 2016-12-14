from tkinter import *
from tkinter import ttk


class View(Frame):
    def __init__(self, master, model):
        """The view that displays the GUI and outputs the simulation data."""
        master.title("Queue simulation")
        master.geometry = model.x_size + "x" + model.y_size
        super(View, self).__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.text_box = Text(self.master, state="disabled", width=80, height=24)
        self.text_box.grid(row=0, column=0)
        self.scrollbar = ttk.Scrollbar(self.master, command=self.text_box.yview)
        self.scrollbar.grid(row=0, column=1, sticky=(N, S))
        self.text_box["yscrollcommand"] = self.scrollbar.set
        self.start_button = Button(self.master, text="Starta")
        self.start_button.grid(row=0, column=2)

    def update_text_box(self, index, text):
        self.text_box["state"] = "normal"
        self.text_box.insert(index, text)
        self.text_box["state"] = "disabled"
