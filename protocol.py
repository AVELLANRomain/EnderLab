from action import ActionController
from layout import Layout, Well
from utils import read, write


def run(action):
    match action["name"]:
        case "load":
            cmd = f"action.load(" + action["well"] + "," + action["volume"] + ")"
            exec(cmd)


class Protocol:
    def __init__(
        self,
        layout: Layout,
        action_controller: ActionController,
        path: str,
        create: bool = False,
    ):
        if create is True:
            protocol = self.create(path)
        protocol = read(path)

        self.layout = layout
        self.controller = action_controller
        self.actions = protocol["actions"]

    def create(self, path: str):
        data = {"name": "", "actions": []}
        write(path, data)
        return data

    def run(self):
        for action in self.actions:
            method = action["name"]

            match method:
                case "pick_cone":
                    module = self._get_module(action["module"])
                    self.controller.pick_cone(module)
                case "eject":
                    self.controller.eject()
                case "change_tips":
                    module = self._get_module(action["module"])
                    self.controller.change_tips(module)
                case "load":
                    well = self._get_well(action["module"], action["well_index"])
                    self.controller.load(well, action["volume"])
                case "drop":
                    module = self._get_module(action["module"])
                    self.controller.load()
                case "move_volume":
                    well_from = self._get_well(
                        action["module_from"], action["well_index_from"]
                    )
                    well_to = self._get_well(
                        action["module_to"], action["well_index_to"]
                    )
                    self.controller.move_volume(well_from, well_to, action["volume"])

    def _get_module(self, module: int):
        return self.layout.module[module]

    def _get_well(self, module: int, well_index: tuple[int, int]) -> Well:
        return self._get_module(module).get_well(well_index)
