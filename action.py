from layout import EJECT_POSITION, Module, Well
from utils import Position


class Action:
    def __init__(self, printer):
        self.printer=printer

    #general comande function: cmd c'est une chaine de character en g code de type "G1 X10 Y18 Z10 E10"
    def cmd(self, cmd):
        comand=cmd+"\n"
        self.printer.write(comand.encode())#encoder la comande
        respons= self.printer.readline().decode().strip()#afficher la reponse du printer
        print(respons)
        
        while respons.lower() != 'ok':# attendre que la comande soit finis
            respons= self.printer.readline().decode().strip()#afficher la reponse du printer
            print(respons)

    # These function has to convert position & high into commands
    def goto(self, position, high):
        """
        Move to max_high
        Move to position
        Move to high
        """
        maxheight=str(50)
        x=str(position[0])
        y=str(position[1])
        z=str(high)

        self.cmd(f"G1 Z{maxheight}")
        self.cmd(f"G1 X{x} Y{y}")
        self.cmd(f"G1 Z{z}")


        print("Go to ", position, high)
        pass


    def pippet(well, volume):
        # Generate command for take

        well.volume -= volume
        print(f"Take volume {volume}")
        print(well.volume)


    def drop(well, volume):
        # Generate command for drop
        well.volume += volume
        print(f"Drop volume {volume}")
        print(well.volume)


    def eject():
        # Generate command for eject
        print(f"Eject")

    def move_volume(self, well_from: Well, well_to: Well, volume: float):
        """Move some volume from one well to another"""
        initial_coord = well_from.module.get_well_coord(well_from.index)
        goto(position=initial_coord.position, high=initial_coord.high)
        take(well_from, volume)

        final_coord = well_to.module.get_well_coord(well_to.index)
        goto(position=final_coord.position, high=final_coord.high)
        drop(well_to, volume)

    def change_tips(self, module: Module):
        self.goto(EJECT_POSITION)
        eject()
        self.goto(module.next_tip)



