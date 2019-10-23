from __future__ import annotations
from typing import Optional, List
from pacActors import *
import pygame
import random

LEVEL_MAPS = ["Level_1.txt"]


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
    === Private Attributes ===
    _running: Determine if game is running or not.
    _level: Current level of the game.
    _max_level: The last level of the game.

    _actors: List of actors in the game.

    === Public Attributes ===
    screen: screen pygame
    player: The player of the game.
    keys_pressed: Key player pressed.
    stage_width: Width of stage.
    stage_height: Height of stage.
    size: Width and height of icon.
    goal_message: A message that tells the player the instructions of the game.
    goal_stars: The amount of stars that the player needs.
    monster_count: The amount of monsters still left to be squished by boxes.
    fire_nation_count: The amount of Fire Nations still left to extinguish.
    keys_collected: The amount of keys player has collected.
    """

    _running: bool
    _level: int
    _max_level: int

    screen: pygame.Surface
    player: Actor
    keys_pressed: tuple
    stage_width: int
    stage_height: int
    size: int
    goal_message: str
    goal_CGPA: int
    
  

    def __init__(self) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        self._level = 0  # Current level that the game is in
        self._max_level = len(LEVEL_MAPS)-1
        self.screen = None
        self.player = None
        self.keys_pressed = None

        # Attributes that get set during level setup
        self._actors = None
        self.stage_width, self.stage_height = 0, 0
        self.size = None
        self.goal_message = None

        # Attributes that are specific to certain levels
        self.goal_CGPA = 0  # Level 0

        # Method that takes care of level setup
        self.setup_current_level()
    def get_level(self) -> int:
        """
        Return the current level the game is at.
        """

        return self._level

    def set_player(self, player: Player) -> None:
        """
        Set the game's player to be the given <player> object.
        """

        self.player = player

    def add_actor(self, actor: Actor) -> None:
        """
        Add the given <actor> to the game's list of actors.
        """

        self._actors.append(actor)

    def remove_actor(self, actor: Actor) -> None:
        """
        Remove the given <actor> from the game's list of actors.
        """

        self._actors.remove(actor)
