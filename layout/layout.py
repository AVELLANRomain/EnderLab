from utils import Coord, Position, read, write

from .module import Module

EJECT_POSITION = Coord(position=Position(x=0, y=500), high=100)


class Layout:

    def __init__(self, origin: Position | None = None):
        self.origin = origin or Position(x=8, y=44)
        self.modules = []

    def create(self, path: str):
        """
        Interface to create layout
        Unit we replace it by GUI
        """
        layout = read("modules.json")
        modules = []

        eppendorf = self.place_module(layout["modules"][0], [4, 4])
        modules.append(eppendorf)

        microplate = self.place_module(layout["modules"][1], [4, 2])
        modules.append(microplate)

        tipsbox = self.place_module(layout["modules"][2], [1, 1])
        modules.append(tipsbox)

        scott25ml = self.place_module(layout["modules"][3], [1, 5])
        modules.append(scott25ml)

        self.save(path, modules)

    def load(self, path: str):
        layout = read(path)
        for module in layout["modules"]:
            self.modules.append(Module(**module))

    def place_module(self, module, index):
        """
        Offset each module position from the grid size
        39 is the case width
        """
        x = self.origin.x + 39 * (index[0] - 1)
        y = self.origin.y + 39 * (index[1] - 1)
        module["position"] = [x, y]
        return module

    def save(self, path: str, modules):
        data = {
            "name": "CMI",
            "dimension": [6, 6],
            "max_high": 105,
            "modules": modules,
        }
        write(path, data)
