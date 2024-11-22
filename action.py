from layout import EJECT_POSITION, Module, Well
from utils import Position


class Action:
    
    def __init__(self, printer):
        self.printer=printer
        self.maxheight=105
        self.eject_pos="G1 X190 Y10"

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
        
        x=str(position.x)
        y=str(position.y)
        z=str(high)
        
        maxh=str(self.maxheight)
        self.cmd(f"G1 Z{maxh}")
        self.cmd(f"G1 X{x} Y{y}")
        self.cmd(f"G1 Z{z}")


        #print("Go to ", position, high)
        pass

    def move_volume(self, well_from: Well, well_to: Well, volume: float):
        """Move some volume from one well to another"""
        initial_coord = well_from.module.get_well_coord(well_from.index)
        #print(initial_coord)
        self.goto(position=initial_coord.position, high=initial_coord.high)
        #take(well_from, volume)

        final_coord = well_to.module.get_well_coord(well_to.index)
        self.goto(position=final_coord.position, high=final_coord.high)
        #drop(well_to, volume)

    def pick_cone(self, tipsbox):
        ok=0
        for col in tipsbox.wells:
            for well in col:
                if well.volume==1:
                    print("toto", well.volume )
                    coord = well.module.get_well_coord(well.index)
                    self.goto(position=coord.position, high=coord.high)
                    self.goto(position=coord.position, high=self.maxheight)
                    ind=well.index 
                    tipsbox.wells[ind[0]][ind[1]].volume=0
                    ok=1
                if(ok == 1):
                    break;
            if(ok == 1):
                break;            
            else:
                print("tipsbox empty")
        return tipsbox
            
    def eject(self):
        maxh=str(self.maxheight)
        self.cmd(f"G1 Z{maxh}")
        self.cmd(self.eject_pos)
        inp = input('eject input')
        print("Eject")

    def change_tips(self, tipsbox):
        self.eject()
        return self.pick_cone(tipsbox)




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


    

    



