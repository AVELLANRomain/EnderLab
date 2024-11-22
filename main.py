from action import Action
from layout import init_layout

import serial
from past.builtins import raw_input

if __name__ == "__main__":
    

    modules = init_layout()
    module = modules[0]
    
    printer=serial.Serial('COM3',115200)
    action = Action(printer)
    
    
    
    
    #test run pour mesurer les mouvement
    # action.cmd("G1 Z40")
    # action.cmd("G1 X-2 Y2")
    # action.move_volume(module.wells[0], module.wells[1], 10)
    
    # action.goto([10,10],10)
    

    # action.move_volume(module.wells[0], module.wells[1], 100)

    # action.change_tips()
