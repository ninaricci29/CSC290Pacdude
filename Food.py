from Actor import *

class Food(Actor):
    """
    A piece of food that pacman can eat to gain points or powerups.
    """
    value = 0.015

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, sprite, value):
        super().__init__(start_xpos, start_ypos, width, height, 0, sprite)
        self.value = value

 # Overrides the Actor's move methods below, since the food cannot move.

    def move_left(self) -> None:
        return None

    def move_right(self) -> None:
        return None

    def move_up(self) -> None:
        return None

    def move_down(self) -> None:
        return None
    
    def getValue(self) -> int:
        return this.value
