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
        self.model.generate_stats()
        self.pause_simulation()

    def run_simulation(self):
        if self.run:
            if self.model.office.is_working:
                self.model.step()
                while self.model.event_handler.has_event:
                    self.view.update_text_box("end", "\n" + self.model.event_handler.get_event())
            else:
                self.end_simulation()
                self.view.update_text_box("end", "\n\n" + self.model.stats)

    def update_parameters(self):
        """Change the values used to simulate"""
        pass
