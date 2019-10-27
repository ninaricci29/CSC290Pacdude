from typing import List
import math, Main, pygame


class Actor(object):
    mvspeed = 0.0
    sprites = {}  # resolution should be RES_WIDTH x RES_HEIGHT



    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, start_mvspeed: float, sprites):
        self.mvspeed = start_mvspeed
        self.sprites = sprites
        self.rect = pygame.Rect(start_xpos, start_ypos, width, height)


    def is_touching(self, other: Actor) -> bool:
        """
        Determines if two Actors are touching each other by rectangular-based collision detection.
        """
        
        return self.rect.colliderect(other.rect)


    def check_left(self, barriers: List[Barrier]) -> bool:
        """
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos - self.mvspeed, self.ypos, self.rect.width, self.rect.height, None)):
                return False
        return True


    def check_right(self, barriers: List[Barrier]) -> bool:
        """
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos + self.mvspeed, self.ypos, self.rect.width, self.rect.height, None)):
                return False
        return True


    def check_up(self, barriers: List[Barrier]) -> bool:
        """
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos, self.ypos - self.mvspeed, self.rect.width, self.rect.height, None)):
                return False
            return True


    def check_down(self, barriers: List[Barrier]) -> bool:
        """
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos, self.ypos + self.mvspeed, self.rect.width, self.rect.height, None)):
                return False
        return True
