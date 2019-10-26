from typing import List
import math, Main, pygame


class Actor(object):
    mvspeed = 0.0
    sprites = {}  # resolution should be RES_WIDTH x RES_HEIGHT

    #def is_touching(self, other: Actor) -> bool:
    #    """
    #    Determines if this object is touching another object, other,
    #    using circular based collision detection.
    #    """
    #
    #    if (math.sqrt(((self.xpos + main.RES_WIDTH) - (other.xpos + main.RES_WIDTH)) ^ 2
    #                  + ((other.xpos + main.RES_WIDTH) - (other.ypos + main.RES_HEIGHT)) ^ 2) <= 10):
    #        return True
    #    return False

    def is_touching(self, other: Actor) -> bool:
        return self.rect.colliderect(other.rect)
        

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, start_mvspeed: float, sprites):
        self.mvspeed = start_mvspeed
        self.sprites = sprites
        self.rect = pygame.Rect(start_xpos, start_ypos, width, height)
