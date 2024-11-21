from utils import Coord, Position, read

from .module import Module, Well

EJECT_POSITION = Coord(position=Position(x=0, y=500), high=100)


def init_layout():
    layout = read("layout.json")
    print(layout)

    # Instanciate layout
    modules = []
    for raw_module in layout["modules"]:
        modules.append(Module(**raw_module))

    return modules

    # Validation
    # we could check if modules fit in layout["dimension"]
