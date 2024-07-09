from House import House

class Second(House):
    def __init__(self):
        #super().__init__(light, tv, gate_unlock, gate_open, sprinklers, door, AC, pool_heater)
        self.light_on = False
        self.tv_on = False
        self.door_open = False
        self.Ac_on = False