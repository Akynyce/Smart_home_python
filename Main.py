from House import House
from First_floor import First
from Basement import Basement
from Second_floor import Second
from Outside import Outside
from Prayer_room import Prayer

Ah = House()
Ha = First()
H = Second()
K = Outside()
Ba = Basement()
Pr = Prayer()

while True:
    print("Smart Home automation")
    print("1 = House control")
    print("2 = First floor control")
    print("3 = Second floor control")
    print("4 = Outside control")
    print("5 = Basement control")
    print("6 = Prayer room control")
    print()

    Ga = int(input("Enter a number from 1 to 6: "))
    if Ga == 1:
        Ah.Lock_gate()
    elif Ga == 2:
        Ha.Lock_door()
    elif Ga == 3:
        H.Switch_on_light()
    elif Ga == 4:
        K.Switch_on_sprinklers()
    elif Ga == 5:
        Ba.Switch_on_pool_heater()
    elif Ga == 6:
        Pr.Auto_switch_on_or_off_AC_room_temperature()
    elif Ga == 7:
        H.Switch_on_light()
    elif Ga == 8:
        Ha.Switch_on_tv()
    elif Ga == 9:
        Ha.Switch_off_tv()
    else:
        print("Invalid input")
