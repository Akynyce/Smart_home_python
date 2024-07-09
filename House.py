is_day = False

class House():
    def __init__(self):
        self.light_on = False  # Initialize light as False (off)
        self.tv_on = False  # Initialize TV as False (off)
        self.gate_unlock = False  # Initialize gate unlock as False (locked)
        self.gate_open = False  # Initialize gate open as False (closed)
        self.sprinklers_on = False  # Initialize sprinklers as False (off)
        self.door_open = False  # Initialize door as False (closed)
        self.Ac_on = False  # Initialize AC as False (off)
        self.pool_heater_on = False  # Initialize pool heater as False (off)

    def Switch_off_light(self):
        if not self.light_on:
            print("Light is already off")
        else:
            self.light_on = False
            print("The light is off")
        return self.light_on  # Return the updated light state

    def Switch_on_light(self):
        if self.light_on:
            print("Light is already on")
        else:
            self.light_on = True
            print("The light is on")
        return self.light_on  # Return the updated light state
    
    def On_light_at_night(self):
        if not self.light_on and not is_day:
            self.light_on = True
            print("Night time, sleep time")
        elif self.light_on and not is_day:
            print("The light was on before the night")
        return self.light_on

    def Off_light_at_day(self):
        if self.light_on and is_day:
            self.light_on = False
            print("Day time, wake up time")
        elif not self.light_on and is_day:
            print("The light was off before the day")
        return self.light_on

    def Switch_off_tv(self):
        if self.tv_on:
            self.tv_on = False
            print("The TV is off")
        else:
            print("It's already off")
        return self.tv_on  # Return the updated TV state

    def Switch_on_tv(self):
        if not self.tv_on:
            self.tv_on = True
            print("The TV is on")
        else:
            print("It's already on")
        return self.tv_on  # Return the updated TV state

    def Unlock_and_open_gate(self):
        if not self.gate_unlock:
            self.gate_unlock = True
            self.gate_open = True
            print("Gate unlocked and opened")
        else:
            print("Gate is already unlocked and open")
        return self.gate_unlock, self.gate_open  # Return the updated gate state

    def Lock_and_close_gate(self):
        if self.gate_unlock:
            self.gate_unlock = False
            self.gate_open = False
            print("Gate locked and closed")
        else:
            print("Gate is already locked and closed")
        return self.gate_unlock, self.gate_open  # Return the updated gate state

    def Unlock_gate(self):
        Unlock_gate_password = input("Enter password: ")
        if not self.gate_unlock and Unlock_gate_password == "Welcome Owner":
            self.gate_unlock = True
            print("The gate is unlocked")
        elif self.gate_unlock and Unlock_gate_password == "Welcome Owner":
            print("Welcome. You left the gate unlocked")
        elif self.gate_unlock and Unlock_gate_password != "Welcome Owner":
            print("The gate is already unlocked, but I don't trust you")
        else:
            print("Wrong password")
        return self.gate_unlock  # Return the updated gate state
    
    def Lock_gate(self):
        if self.gate_unlock:
            self.gate_unlock = False
            print("The gate is locked")
        else:
            print("The gate is already locked")
        return self.gate_unlock  # Return the updated gate state
    
    def open_gate(self):
        if self.gate_unlock and not self.gate_open:
            self.gate_open = True
            print("Gate opened")
        elif not self.gate_unlock:
            print("Cannot open gate: it is locked")
        else:
            print("Gate is already open")
        return self.gate_open

    def close_gate(self):
        if self.gate_open:
            self.gate_open = False
            print("Gate closed")
        else:
            print("Gate is already closed")
        return self.gate_open
    
    def Switch_off_sprinklers(self):
        if self.sprinklers_on:
            self.sprinklers_on = False
            print("The sprinklers are off")
        else:
            print("It's already off")
        return self.sprinklers_on  # Return the updated sprinklers state
    
    def Switch_on_sprinklers(self):
        if not self.sprinklers_on:
            self.sprinklers_on = True
            print("The sprinklers are on")
        else:
            print("It's already on")
        return self.sprinklers_on  # Return the updated sprinklers state
    
    def Lock_door(self):
        Lock_door_password = input("Enter password: ")
        if self.door_open and Lock_door_password == "My Space":
            self.door_open = False
            print("The door is locked")
        elif self.door_open and Lock_door_password != "My Space":
            print("Wrong password. The door is not locked")
        elif not self.door_open:
            print("The door is already locked")
        return self.door_open  # Return the updated door state
    
    def Unlock_door(self):
        Unlock_door_password = input("Enter password: ")
        if not self.door_open and Unlock_door_password == "My Space":
            self.door_open = True
            print("The door is unlocked")
        elif self.door_open:
            print("The door is already unlocked")
        else:
            print("Wrong password. The door is not unlocked")
        return self.door_open  # Return the updated door state
    
    def Switch_off_Ac(self):
        if self.Ac_on:
            self.Ac_on = False
            print("The AC is off")
        else:
            print("It's already off")
        return self.Ac_on  # Return the updated AC state

    def Switch_on_Ac(self):
        if not self.Ac_on:
            self.Ac_on = True
            print("The AC is on")
        else:
            print("It's already on")
        return self.Ac_on  # Return the updated AC state
    
    def Auto_switch_on_or_off_AC_room_temperature(self):
        on_or_off_AC = float(input("Enter the room's temperature: "))
        if 25 <= on_or_off_AC <= 50:
            self.Switch_on_Ac()
        elif 0 <= on_or_off_AC < 25:
            self.Switch_off_Ac()
        else:
            print("Invalid temperature. The AC remains the same.")
        return self.Ac_on  # Return the updated AC state

    def Switch_off_pool_heater(self):
        if self.pool_heater_on:
            self.pool_heater_on = False
            print("The pool heater is off")
        else:
            print("It's already off")
        return self.pool_heater_on  # Return the updated pool heater state

    def Switch_on_pool_heater(self):
        if not self.pool_heater_on:
            self.pool_heater_on = True
            print("The pool heater is on")
        else:
            print("It's already on")
        return self.pool_heater_on  # Return the updated pool heater state
    
    def Auto_switch_on_or_off_pool_heater_pool_temperature(self):
        on_or_off_pool_heater = float(input("Enter the pool's temperature: "))
        if -15 <= on_or_off_pool_heater < 25:
            self.Switch_on_pool_heater()
        elif 25 <= on_or_off_pool_heater <= 70:
            self.Switch_off_pool_heater()
        else:
            print("Invalid temperature. The pool heater remains the same.")
        return self.pool_heater_on  # Return the updated pool heater state