import requests

from settings import DEV_MODE, FAKE

if DEV_MODE:
    URL = "http://localhost"
else:
    URL = "http://192.168.1.141:5000"


def call_cmd(command: str):
    if FAKE is True:
        print(command)
        return
    response = requests.get(f"{URL}/cmd", params={"cmd": command})
    print(response.text)


def call_eject():
    if FAKE is True:
        print("elect")
        return
    response = requests.get(f"{URL}/eject")
    print(response.text)
