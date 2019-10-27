from typing import List
import math, Main, pygame, Barrier


class Actor(object):
    """
    An Actor/Entity in a game of pacman. An Actor is a rectangle that
    has a set of coordinates, dimensions, sprites and complies with a 
    basic physics engine.
    """
    
    mvspeed = 0.0
    sprites = {}  # resolution should be RES_WIDTH x RES_HEIGHT


    def __init__(self, start_xpos: float, start_ypos: float, \
                 width: float, height: float, start_mvspeed: float, sprites):
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
        Determines if moving leftwards would put the Actor inside of a barrier.
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos - self.mvspeed, self.ypos, \
                                         self.rect.width, self.rect.height, None)):
                return False
        return True


    def check_right(self, barriers: List[Barrier]) -> bool:
        """
        Determines if moving rightwards would put the Actor inside of a barrier.
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos + self.mvspeed, self.ypos, \
                                         self.rect.width, self.rect.height, None)):
                return False
        return True


    def check_up(self, barriers: List[Barrier]) -> bool:
        """
        Determines if moving upwards would put the Actor inside of a barrier.
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos, self.ypos - self.mvspeed, \
                                         self.rect.width, self.rect.height, None)):
                return False
            return True


    def check_down(self, barriers: List[Barrier]) -> bool:
        """
        Determines if moving downwards would put the Actor inside of a barrier.
        """

        for barrier in barriers:
            if barrier.is_touching(Actor(self.xpos, self.ypos + self.mvspeed, \
                                         self.rect.width, self.rect.height, None)):
                return False
        return True

    
    def move_left(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving leftwards would put Actor inside of a barrier.
            If that is not the case, then move Actor right by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "left" entry in self.sprites
        """

        if (self.check_left(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos - self.mvspeed, self.ypos)


    def move_right(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving rightwards would put Actor inside of a barrier.
            If that is not the case, then move Actor right by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "right" entry in self.sprites
        """

        if (self.check_right(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos + self.mvspeed, self.ypos)


    def move_up(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving upwards would put Actor inside of a barrier.
            If that is not the case, then move Actor up by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "up" entry in self.sprites
        """

        if (self.check_up(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos, self.ypos - self.mvspeed)


    def move_down(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving downwards would put Actor inside of a barrier.
            If that is not the case, then move Actor down by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "down" entry in self.sprites
        """

        if (self.check_down(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos, self.ypos + self.mvspeed)