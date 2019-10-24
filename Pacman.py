from typing import List

class Pacman(Actor):
    movement_direction = 0 #0 : left, 1 : up, 2 : right, 3 : down

    def __init__(self, start_xpos: float, start_ypos: float):
        super().__init__(start_xpos, start_ypos, 5,
                         {"left": None, "right": None, "bottom": None, "up": None})

    def Move(self, barriers: List):
        #TODO: implement this
        # variable movement_direction specifies the direction pacman is going
        pass
