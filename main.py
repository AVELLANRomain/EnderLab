from action import Action
from layout import init_layout

if __name__ == "__main__":
    modules = init_layout()
    module = modules[0]

    action = Action()
    action.move_volume(module.wells[0], module.wells[1], 100)

    # action.change_tips()
