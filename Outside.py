from House import House

class Outside(House):
    def __init__(self):
        self.light = False
        self.sprinklers_on = False
        self.gate_open = False
        self.gate_unlock = False