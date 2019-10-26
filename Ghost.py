from typing import List
import pygame, Actor

class Ghost(Actor):
    
    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, start_mvspeed: float, sprites: dict):
        super().__init__(start_xpos, start_ypos, width, height, start_mvspeed, sprites)

    
    def chase_pacman(self, pacman: Actor) -> None:
        