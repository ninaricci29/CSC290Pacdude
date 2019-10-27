from typing import List
import Actor, Barrier

class Pacman(Actor):
    """
    The playable character of the game.
    """

    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, sprites: dict):
        super().__init__(start_xpos, start_ypos, 5, sprites)

    def move_left(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving leftwards would put pacman inside of a barrier.
            If that is not the case, then move pacman right by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "left" entry in self.sprites
        """

        if (self.check_left(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos - self.mvspeed, self.ypos)

    
    def move_right(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving rightwards would put pacman inside of a barrier.
            If that is not the case, then move pacman right by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "right" entry in self.sprites
        """

        if (self.check_right(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos + self.mvspeed, self.ypos)

    
    def move_up(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving upwards would put pacman inside of a barrier.
            If that is not the case, then move pacman up by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "up" entry in self.sprites
        """

        if (self.check_up(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos, self.ypos - self.mvspeed)

    
    def move_down(self, barriers: List[Barrier]) -> None:
        """
            Determines if moving downwards would put pacman inside of a barrier.
            If that is not the case, then move pacman down by mv_speed,
            and update his sprite accordingly.

            Precondition: There exists a "down" entry in self.sprites
        """

        if (self.check_down(barriers)):
            #TODO: change sprite appropriately
            self.rect.move(self.xpos, self.ypos + self.mvspeed)
