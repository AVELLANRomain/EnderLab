def run(action):
    match action["name"]:
        case "load":
            cmd = f"action.load(" + action["well"] + "," + action["volume"] + ")"
            exec(cmd)
