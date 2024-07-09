from House import House

class Prayer(House):
    def __init__(self):
        #super().__init__(light, door, AC)
        self.light_on = False
        self.door_open = False
        self.Ac_on = False