from __future__ import annotations
import pygame
from typing import Optional
from settings import *

class Actor:
    """
    A class that represents the game's actors and includes any
    attributes/methods that every actor in the game must have.

    This is an abstract class. Only subclasses should be instantiated.

    === Public Attributes ===
    x:
        x coordinate of this actor's location on the stage
    y:
        y coordinate of this actor's location on the stage
    icon:
        the image representing this actor
    """
    x: int
    y: int
    icon: pygame.Surface

    def __init__(self, icon, x, y):
        """Initialize an actor with the given image <icon> and the
        given <x> and <y> position on the game's stage.
        """

        self.x, self.y = x, y
        self.icon = pygame.image.load(icon)

    def move(self, game: 'Game') -> None:
        """Move this actor. """

        raise NotImplementedError
