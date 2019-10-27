from typing import List
import Actor, Barrier

class Pacman(Actor):
    """
    The playable character of the game.
    """

    def __init__(self, start_xpos: float, start_ypos: float, \
                 width: float, height: float, sprites: dict):
        super().__init__(start_xpos, start_ypos, 5, sprites)