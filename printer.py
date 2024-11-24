from tests import FakeConnexion


class Printer:
    OK = "ok"

    def __init__(self, fake: bool = False):
        if fake is True:
            self.connexion = FakeConnexion()
        else:
            import serial

            self.connexion = serial.Serial("COM3", 115200)

    def write(self, command: str):
        self.connexion.write(f"{command}\n".encode())

    def read(self) -> str:
        response = self.connexion.readline()
        return response.decode().strip().lower()
