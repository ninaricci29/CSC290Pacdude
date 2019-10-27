from __future__ import annotations
from typing import Optional, List
import Actor, Barrier, Food, Ghost, Pacman
from pygame import *
import random

MAP = ["Level_1.txt"]

def load_map(filename: str) -> List[List[str]]:
    """
    Load the map data from the given filename and return as a list of lists.
    """

    with open(filename) as f:
        map_data = [line.split() for line in f]
    return map_data

class Game:
    """
    This class represents the main game.
    """

    _running: bool
    _level: int
    _max_level: int

    
    keys_pressed: tuple

    screen: pygame.Surface
    stage_width: int
    stage_height: int
    size: int

    goal_message: str
    goal_CGPA: float
    current_CGPA : float

    player: Pacman
    barriers : List[Barrier] # TODO: generate the list of barriers from the map text files
    ghosts : List[Ghost] # TODO: generate the list of ghosts
    foods : List[Food] # TODO: genereate the list of food


    def __init__(self) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        self._level = 0  # Current level that the game is in
        self.screen = None
        self.player = Pacman(None, None, None, None, {}) # TODO: fill out the constructor's parameters appropriately
        self.keys_pressed = None

        # Attributes that get set during level setup
        self._actors = None
        self.stage_width, self.stage_height = 0, 0
        self.size = None
        self.goal_message = None

        # Attributes that are specific to certain levels
        self.goal_CGPA = 0  # Level 0

        # Method that takes care of level setup
        self.setup_level()


    def execute(self) -> None:
        """
        Holds the main game loop of the game, which performs actions
        such as checking for user input, making the ghosts chase pacman, etc.
        on a continuous basis. Runs until is_game_over() returns true.
        """

        is_game_over = False
        pygame.init()

        while (not is_game_over):
            
            # Handle user input. Arrow keys control the player's movement.
            for event in pygame.event.get():
                if (event.key == pygame.K_LEFT):
                    player.move_left(barriers)
                elif (event.key == pygame.K_RIGHT):
                    player.move_right(barriers)
                elif (event.key == pygame.K_UP):
                    player.move_up(barriers)
                elif (event.key == pygame.K_DOWN):
                    player.move_down(barriers)

            # Make all of the ghosts chase pacman and checks if one of them has caught pacman
            for ghost in ghosts:
                ghost.chase_pacman(player, barriers)
                if (ghost.is_touching(player)):
                    is_game_over = True

            # Add to score whenever pacman eats a piece of food
            for food in foods:
                if (food.is_touching(player)):
                    current_cgpa += food.value