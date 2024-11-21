import uuid

from utils import Coord, Position


class Module:
    def __init__(
        self, name, wells, position: list[float], hauteur=None, *args, **kwargs
    ):
        self.id = uuid.uuid4()
        self.name = name
        self.wells = self.create_wells(wells)
        self.position = Position.from_list(position)
        self.hauteur = hauteur

    def create_wells(self, raw_wells: list[dict]):
        wells = []
        for index, well in enumerate(raw_wells):
            name = well.pop("name", f"well_{index}")
            raw_position = well.pop("position")
            position = Position.from_list(raw_position)
            wells.append(
                Well(module=self, index=index, name=name, position=position, **well)
            )
        return wells

    def get_well_coord(self, index):
        well = self.wells[index]
        hauteur = self.hauteur if self.hauteur is not None else well.hauteur
        return Coord(self.position.add(well.position), hauteur)


class Well:
    def __init__(
        self,
        index,
        module: Module,
        position,
        volume_max,
        name=None,
        volume=0,
        hauteur=None,
        **kwargs,
    ):
        self.index = index
        self.module = module
        self.name = name or self.id
        self.volume_max = volume_max
        self.position = position
        self.volume = volume
        self.hauteur = hauteur

    @property
    def id(self):
        return f"{self.module.id}__{self.index}"
