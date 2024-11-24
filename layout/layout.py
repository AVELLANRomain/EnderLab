from utils import Coord, Position, read

from .module import Module, Well

EJECT_POSITION = Coord(position=Position(x=0, y=500), high=100)


def init_layout():
    layout = read("modules.json")
    #print(layout)

    # Instanciate layout
    modules = []
    
    eppendorf=crate_module(layout["modules"][0],[4,4])
    modules.append(Module(**eppendorf))
    
    microplate = crate_module(layout["modules"][1],[4,2])
    modules.append(Module(**microplate))
    
    tipsbox=crate_module(layout["modules"][2],[1,1])
    modules.append(Module(**tipsbox))
    
    scott25ml=crate_module(layout["modules"][3],[1,5])
    modules.append(Module(**scott25ml))
    
    # for raw_module in layout["modules"]:
    #     modules.append(Module(**raw_module))

    return modules

    # Validation
    # we could check if modules fit in layout["dimension"]


def crate_module(module, index):
    x=8+39*(index[0]-1)
    y=44+39*(index[1]-1)
    pos=[x,y]
    module["position"]=pos
    return module
    
    
