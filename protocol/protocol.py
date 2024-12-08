import json

from layout import Layout, Well
from protocol.action import ActionController
from utils import read, write


def run(action):
    match action["name"]:
        case "load":
            cmd = f"action.load(" + action["well"] + "," + action["volume"] + ")"
            exec(cmd)


class Instruction:
    def __init__(self, layout: Layout, action: dict):
        self.layout = layout
        self.controller = ActionController()
        self.action = action

    def run(self):
        method = self.action["name"]

        match method:
            case "pick_cone":
                module, _ = self.action["well_index"]
                module = self._get_module(module)
                self.controller.pick_cone(module)
            case "eject":
                self.controller.eject()
            case "change_tips":
                module, _ = self.action["well_index"]
                module = self._get_module(module)
                self.controller.change_tips(module)
            case "load":
                module, well_index = self.action["well_index"]
                well = self._get_well(module, well_index)
                self.controller.load(well, self.action["volume"])
            case "drop":
                module, well_index = self.action["well_index"]
                well = self._get_well(module, well_index)
                self.controller.drop(well, self.action["volume"])
            case "mix":
                module, well_index = self.action["well_index"]
                well = self._get_well(module, well_index)
                self.controller.mix(well, self.action["volume"], self.action["number"])
            case "move_volume":
                module_from, well_index_from = self.action["well_index_from"]
                well_from = self._get_well(module_from, well_index_from)
                module_to, well_index_to = self.action["well_index_to"]
                well_to = self._get_well(module_to, well_index_to)
                self.controller.move_volume(well_from, well_to, self.action["volume"])

    def _get_module(self, module: int):
        return self.layout.modules[module]

    def _get_well(self, module: int, well_index: tuple[int, int]) -> Well:
        return self._get_module(module).get_well(well_index)

    def __str__(self):
        return {**self.action}

    def __repr__(self):
        return f"Instruction ({json.dumps({**self.action})})"


class Protocol:
    def __init__(
        self,
        name: str,
        layout: Layout,
        steps: list[dict] | dict,
        mapping: dict,
        elementary: bool = False,
    ):
        self.name = name
        self.layout = layout
        self.mapping = mapping
        self.elementary = elementary

        if self.elementary is True:
            self.steps = steps
        else:
            self.steps = self.load_protocol(steps)

    def load_protocol(self, steps: list[dict]) -> "Protocol":
        protocols = []
        for step in steps:
            protocols.append(
                Protocol(
                    name=step["name"],
                    layout=self.layout,
                    steps=step["steps"],
                    mapping=step["mapping"],
                    elementary=step["elementary"],
                )
            )
        return protocols

    def run(self):
        instructions = self.build_instructions(self.mapping)
        print(instructions)
        for instruction in instructions:
            instruction.run()

    def build_instructions(self, parent_mapping: dict) -> list[Instruction]:
        instructions = []

        if self.elementary is True:
            action = self.steps

            match action["name"]:
                case "mix":
                    for well_id, value in parent_mapping["wells"].items():
                        if well_id == action["well_index"]:
                            action["well_index"] = value
                    for param, value in parent_mapping["params"].items():
                        if param == action["volume"]:
                            action["volume"] = value
                        elif param == action["number"]:
                            action["number"] = value

                case "mouve_volume":
                    for well_id, value in parent_mapping["wells"].items():
                        if well_id == action["well_index_from"]:
                            action["well_index_from"] = value
                        if well_id == action["well_index_to"]:
                            action["well_index_to"] = value
                    for param, value in parent_mapping["params"].items():
                        if param == action["volume"]:
                            action["volume"] = value
                case "change_tips":
                    for well_id, value in parent_mapping["wells"].items():
                        if well_id == action["well_index"]:
                            action["well_index"] = value
                case "pick_cone":
                    for well_id, value in parent_mapping["wells"].items():
                        if well_id == action["well_index"]:
                            action["well_index"] = value

            instructions.append(Instruction(layout=self.layout, action=action))
        else:
            for protocol in self.steps:
                if isinstance(protocol, Protocol):
                    mapping_resolved = {**protocol.mapping}

                    for well_id, value in mapping_resolved["wells"].items():
                        if value in list(parent_mapping["wells"].keys()):
                            mapping_resolved["wells"][well_id] = parent_mapping[
                                "wells"
                            ][value]

                    for param, value in mapping_resolved["params"].items():
                        if value in list(parent_mapping["params"].keys()):
                            mapping_resolved["params"][param] = parent_mapping[
                                "params"
                            ][value]

                    instructions.extend(protocol.build_instructions(mapping_resolved))

        return instructions

    def to_dic(self, protocol):
        if protocol.elementary is True:
            dic = {
                "name": protocol.name,
                "elementary": protocol.elementary,
                "mapping": protocol.mapping,
                "steps": protocol.steps,
            }
            return dic
        else:
            dic = {
                "name": protocol.name,
                "elementary": protocol.elementary,
                "mapping": protocol.mapping,
                "steps": [],
            }
            for step in protocol.steps:
                dic["steps"].append(self.to_dic(step))
            return dic


class ProtocolRepository:
    def __init__(self, layout: Layout):
        self.layout = layout

    def get(self, path: str):
        data = read(path)

        return Protocol(
            name=data["name"],
            layout=self.layout,
            steps=data["steps"],
            mapping=data["mapping"],
            elementary=data["elementary"],
        )

    def create(self, path: str, data: dict):
        write(path, data)
        return data
