from layout import Layout
from protocol.action import ActionController
from protocol.protocol import ProtocolRepository


def printer_init():
    action = ActionController()
    # go over the layout
    action.cmd("G1 Z105")  # hauteur max
    # action.cmd("G1 Z105 F10") #F**** vitesse de deplacement en Z
    # auto home axis X and Y
    action.cmd("G28 X Y")
    # disable cold extrusion safty
    action.cmd("M302 P1")


if __name__ == "__main__":
    # Init printer
    printer_init()

    layout = Layout()
    # First time
    # layout.create(path="data/layout_1.json")
    # Usage
    layout.load(path="data/layout_1.json")

    # Instantiate Protocol
    repo = ProtocolRepository(layout=layout)
    protocol = repo.get(path="data/multimix.json")

    protocol.run()

    protocol = repo.get(path="data/mix.json")

    protocol.run()

    ##### TEST hardware #####
    # action = ActionController()

    # eppendorf = layout.modules[0]
    # microplate = layout.modules[1]
    # tipsbox = layout.modules[2]
    # scott25ml = layout.modules[3]

    # set travel limit
    # action.cmd("M503") #print setings
    # action.cmd("M208 X200 Y200 Z90")

    # test protocol alliquotage
    # tipsbox = action.pick_cone(tipsbox)
    # action.load(scott25ml.wells[0][0], 10)
    # action.drop(eppendorf.wells[0][0], 100)

    # test run pour mesurer les mouvement
    # action.cmd("G1 Z105")  # hauteur max
    # action.cmd("G1 X8 Y44")  # origine

    # teste possition connes
    # action.cmd("G1 Z56")  # au dessu des connes
    # action.cmd("G1 Z53")  # dedan pour parametre
    # action.cmd("G1 Z48")  # pick up conne
    # action.cmd("G1 Z105")  # hauteur max connes

    # action.cmd("G1 X16 Y70.8")  # tips 0,0
    # action.cmd("G1 X115 Y115.8")  # corner

    # action de connes
    # tipsbox = action.pick_cone(tipsbox)
    # action.eject()
    # tipsbox = action.change_tips(tipsbox)

    # test pour les eppendorf
    # action.cmd("G1 Z65")  # hauteur des puits
    # action.cmd("G1 X17 Y50")  # puits 0,0

    # action de pipetage
    # action.load(eppendorf.wells[0][0], 10)
    # action.drop(microplate.wells[0][0], 10)
    # action.move_volume(microplate.wells[0][0], microplate.wells[1][1], 10)
    # action.move_volume(eppendorf.wells[0][0], eppendorf.wells[1][1], 10)
