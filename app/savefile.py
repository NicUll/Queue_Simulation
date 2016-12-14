class SaveFile(object):
    def __init__(self, filename):
        """An object responsible for handling the savefile"""
        self.filename = filename
        self.time_per_customer = 2
        self.open_times = ("09:00", "18:00")
        self.new_customer_odds = 0.2
        self.errands_per_customer = None
        self.fetch_data()

    def fetch_data(self):
        try:
            with open(self.filename, "r") as file:
                self.time_per_customer = int(file.readline())
                self.open_times = file.readline().split(",")
                self.new_customer_odds = float(file.readline())
        except FileNotFoundError:
            with open(self.filename, "w") as file:

                file.write("{}\n{},{}\n{}".format(self.time_per_customer, self.open_times[0], self.open_times[1],
                                                       self.new_customer_odds))

    def save_data(self, time_per_customer, open_times, new_customer_odds):
        with open(self.filename, "w") as file:
            file.write("{}\n{},{}\n{}".format(time_per_customer, open_times[0], open_times[1],
                                                   new_customer_odds))
