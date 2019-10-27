from typing import List
import pygame, Actor, Barrier, math

class Ghost(Actor):
    """
        The adversary of the game. Chases pacman using rudimentary pathfinding A.I.
        The game ends when pacman is "caught" by a ghost.
        """

    move_direction: str  # move_direction must be in {"left", "right", "up", "down"}

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, start_mvspeed: float, sprites: dict):
        super().__init__(start_xpos, start_ypos, width, height, start_mvspeed, sprites)

    def chase_pacman(self, pacman: Actor) -> None:
        """
        Pathfinding A.I. for the ghosts. First, checks if the Ghost is at an intersection.
        If it is, then change the move_direction of the ghost to the one with the shortest
        distance to pacman. If not, continue moving along move_direction.
        Preconditions: move_direction must be in {"left", "right", "up", "down"}
        """
        x_dist = pacman.rect.xpos - self.rect.xpos
        y_dist = pacman.rect.ypos - self.rect.ypos

        # first, determine if the ghost is at an intersection. If it is, then change direction.
        if (self.check_left(barriers) and self.check_right(barriers) \
                and self.check_up(barriers) and self.check_down(barriers)):
            # change direction to the one with the shortest distance to pacman.
            if (math.abs(x_dist) > math.abs(y_dist) and x_dist > 0):
                self.move_direction = "right"
            elif (math.abs(x_dist) > math.abs(y_dist) and x_dist < 0):
                self.move_direction = "left"
            elif (math.abs(y_dist) > math.abs(x_dist) and y_dist > 0):
                self.move_direction = "down"
            elif (math.abs(y_dist) > math.abs(x_dist) and y_dist < 0):
                self.move_direction = "up"
        else:
            # If the ghost is not at an intersection, then continue moving in the move_direction.
            if (self.move_direction == "right"):
                self.move_right(barriers)
            elif (self.move_direction == "left"):
                self.move_left(barriers)
            elif (self.move_direction == "down"):
                self.move_down(barriers)
            elif (self.move_direction == "up"):
                self.move_up(barriers)
        y_dist = pacman.rect.ypos - self.rect.ypos