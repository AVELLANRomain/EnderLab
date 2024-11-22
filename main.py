from action import Action
from layout import init_layout

import serial
from past.builtins import raw_input

if __name__ == "__main__":
    

    modules = init_layout()
    #eppendorf=modules[0] #a repositionner
    #microplate = modules[1] #a repositionner
    tipsbox=modules[2]
    
    
    printer=serial.Serial('COM3',115200)
    action = Action(printer)
    
    # go over the layout
    action.cmd("G1 Z105") #hauteur max
    # auto home axis X and Y
    action.cmd("G28 X Y")
    
    
    #test run pour mesurer les mouvement
    # action.cmd("G1 Z105") # hauteur max
    # action.cmd("G1 X8 Y44") # origine
    
    #teste possition connes
    # action.cmd("G1 Z56") # au dessu des connes
    # action.cmd("G1 Z53") # dedan pour parametre
    # action.cmd("G1 Z48") #pick up conne
    # action.cmd("G1 Z105") # hauteur max connes
    
    # action.cmd("G1 X16 Y70.8") # tips 0,0
    # action.cmd("G1 X115 Y115.8") # corner
    
    #action de connes
    # tipsbox=action.pick_cone(tipsbox)
    # action.eject()
    # tipsbox=action.change_tips(tipsbox)
    
    
    
    
    
    #test pour les eppendorf
    # action.cmd("G1 Z65") # hauteur max eppendorf
    
    
    #eject position :
    # action.cmd("G1 X180 Y-20")
    
    
    
    
    #action de pipetage
    # action.move_volume(microplate.wells[0][0], microplate.wells[1][1], 10)
    # action.move_volume(eppendorf.wells[0], eppendorf.wells[1], 10)
    
    

    # action.move_volume(module.wells[0], module.wells[1], 100)

    # action.change_tips()
