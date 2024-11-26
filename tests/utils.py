import time
from random import random


class FakeConnexion:
    def __init__(self, latency=0.05):
        self.latency = latency

    def write(self, command: str) -> str:
        time.sleep(self.latency)
        #print(command)

    def readline(self) -> str:
        time.sleep(self.latency)
        return self._get_response().encode()

    def _get_response(self):
        p = random()
        if p < 0.2:
            return "OK"
        return "null"
