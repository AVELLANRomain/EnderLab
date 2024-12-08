from protocol.protocol import ProtocolRepository, Protocol
import json


def create_new_protocol(layout):
    # name = input("protocol name?\n")
    name = "test"
    protocol = Protocol(
        name=name,
        layout=layout,
        steps=[],
        mapping={"wells": {}, "params": {}},
        elementary=False,
    )
    return protocol


def add_step(protocol, step):
    for key, value in step.mapping["wells"].items():
        # print(key, value)
        name = input(f"{key} name?\n")
        valeur = input(f"{key} valeur?\n")

        step.mapping["wells"][key] = name
        protocol.mapping["wells"][name] = eval(valeur)

    for key, value in step.mapping["params"].items():
        # print(key, value)
        name = input(f"{key} name?\n")
        valeur = input(f"{key} valeur?\n")

        step.mapping["params"][key] = name
        protocol.mapping["params"][name] = eval(valeur)

    protocol.steps.append(step)
    return protocol
