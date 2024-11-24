

def run(action):
    match action["name"]:
        case "load":
            cmd=f"action.load("+action["well"]+","+ action["volume"]+")"
            exec(cmd)
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print(f"{day} is a weekday.")
        case _:
            print("That's not a valid day of the week.")