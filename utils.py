import json
from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float

    @classmethod
    def from_list(cls, position: list):
        return Position(x=position[0], y=position[1])

    def add(self, position):
        return Position(x=self.x + position.x, y=self.y + position.y)


@dataclass
class Coord:
    position: Position
    high: float


def read(path):
    with open(path) as f:
        return json.load(f)
