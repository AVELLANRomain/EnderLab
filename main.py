from action import Action
from layout import init_layout

import serial
from past.builtins import raw_input

if __name__ == "__main__":
    printer=serial.Serial('COM3',115200)

    modules = init_layout()
    module = modules[0]

    action = Action(printer)
    #test run pour mesurer les mouvement
    # action.cmd("G1 Z40")
    # action.goto([10,10],10)
    

    # action.move_volume(module.wells[0], module.wells[1], 100)

    # action.change_tips()
