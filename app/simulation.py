from app.model import Model


class Simulation(object):
    def __init__(self, view, model, speed):
        """Runs the simulation with the current simulation
        parameters."""
        self.speed = speed  # The simulation speed
        self.model = model
        self.view = view
        self.run = False

    def start_simulation(self):
        self.run = True

    def pause_simulation(self):
        self.run = False

    def end_simulation(self):
        self.pause_simulation()
        self.model.generate_stats()

    def update_parameters(self):
        """Change the values used to simulate"""
        pass
