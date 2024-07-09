from House import House

class Basement(House):
    def __init__(self):
        self.light_on = False
        self.tv_on = False
        self.door_open = False
        self.Ac_on = False
        self.pool_heater_on = False