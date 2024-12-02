import requests

DEV_MODE = False

if DEV_MODE:
    URL = "http://localhost"
else:
    URL = "http://192.168.1.141:5000"


def call_cmd(command: str):
    response = requests.get(f"{URL}/cmd", params={"cmd": command})
    print(response.text)


def call_eject():
    response = requests.get(f"{URL}/eject")
    print(response.text)
