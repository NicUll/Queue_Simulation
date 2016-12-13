from tkinter import *


class View(Frame):
    def __init__(self, master, model):
        """The view that displays the GUI and outputs the simulation data."""
        master.title("Queue simulation")
        master.geometry = model.x_size + "x" + model.y_size
        self.root = master
        super(View, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.text_box = Text(self.root, state="disabled", width=80, height=24)
        self.text_box.grid()

    def update_text_box(self, index, text):
        self.text_box["state"] = "normal"
        self.text_box.insert(index, text)
        self.text_box["state"] = "disabled"

