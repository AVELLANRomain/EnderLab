from layout import EJECT_POSITION, Module, Well
from utils import Position


class Action:
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


# These function has to convert position & high into commands


def goto(position, high):
    """
    Move to max_high
    Move to position
    Move to high
    """
    print("Go to ", position, high)
    max_high = ...
    pass


def take(well, volume):
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
