from layout import Module, Well
from printer import Printer


class ActionController:

    def __init__(self, printer: Printer):
        self.printer = printer
        self.maxheight = 105
        self.eject_pos = "G1 X190 Y10"

    def cmd(self, command):
        """
        General command function
        command example: "G1 X10 Y18 Z10 E10"
        """
        self.printer.write(command)
        response: str | None = None

        # Wait until command has finished
        while response != Printer.OK:
            response = self.printer.read()
            # time.sleep(0.1)  # Wait for 0.1 second
            print(response)

    # These function has to convert position & high into commands
    def goto(self, position, high):
        """
        Move to max_high
        Move to position
        Move to high
        """

        x = str(position.x)
        y = str(position.y)
        z = str(high)

        maxh = str(self.maxheight)
        self.cmd(f"G1 Z{maxh}")
        self.cmd(f"G1 X{x} Y{y}")
        self.cmd(f"G1 Z{z}")

        # print("Go to ", position, high)

    def pick_cone(self, tipsbox: Module):
        for col in tipsbox.wells:
            for well in col:
                if well.volume == 1:
                    coord = well.module.get_well_coord(well.index)
                    self.goto(position=coord.position, high=coord.high)
                    self.goto(position=coord.position, high=self.maxheight)
                    tipsbox.wells[well.index[0]][well.index[1]].volume = 0
                    return tipsbox

        print("tipsbox empty")
        return tipsbox

    def eject(self):
        self.cmd(f"G1 Z{self.maxheight}")
        self.cmd(self.eject_pos)
        inp = input("eject input")
        print("Eject")

    def change_tips(self, tipsbox: Module):
        self.eject()
        return self.pick_cone(tipsbox)

    def load(self, well: Well, volume: float) -> Well:
        """
        Take a volume from the well
        """
        print("load ", volume)
        if volume <= well.volume:
            coord = well.module.get_well_coord(well.index)
            self.goto(position=coord.position, high=well.load_height)
            self.cmd(f"G1 E-{mltostep(volume)}")
            well.volume = well.volume - volume
        else:
            print(f"not enough volume in {well.name}")

    def drop(self, well, volume):
        print("drop ", volume)
        if volume + well.volume <= well.volume_max:
            coord = well.module.get_well_coord(well.index)
            self.goto(position=coord.position, high=coord.high)
            self.cmd("G1 E20")
            self.cmd("G1 E0")
            well.volume = well.volume + volume
        else:
            print(f"not enough room in {well.name}")

    def mix(self, well, volume, number):
        if volume <= well.volume:
            coord = well.module.get_well_coord(well.index)
            self.goto(position=coord.position, high=well.load_height)

            i = 0
            while i < number:
                self.cmd(f"G1 E-{mltostep(volume)}")
                self.cmd(f"G1 E{mltostep(volume)}")
                i += 1
            self.drop(well, 0)
        else:
            print(f"not enough volume in {well.name}")

    def move_volume(self, well_from: Well, well_to: Well, volume: float):
        """Move some volume from one well to another"""
        well_from = self.load(well_from, volume)
        well_to = self.drop(well_to, volume)


def mltostep(volume: float):
    """
    Volume alibration function
    """
    step = (13 / 100) * volume
    return step
