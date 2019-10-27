from __future__ import annotations
from typing import Optional, List
from Actor import *
from Barrier import *
from Ghost import *
from Food import *
from Pacman import *
from pygame import *
import random

MAP = ["Map.txt"]
ICON_SIZE = 24

def load_map(filename: str) -> List[List[str]]:
    """
    Load the map data from the given filename and return as a list of lists.
    """

    with open(filename) as f:
        map_data = [line.split() for line in f]
    return map_data


class Game:
    ICON_SIZE = 24
    """
    This class represents the main game.
    """

    _running: bool
    _max_level: int

    keys_pressed: tuple

    screen: pygame.Surface
    stage_width: int
    stage_height: int
    size: int

    goal_message: str
    goal_CGPA: float
    current_CGPA: float

    player: Pacman
    barriers: List[Barrier]  # TODO: generate the list of barriers from the map text files
    ghosts: List[Ghost]  # TODO: generate the list of ghosts
    foods: List[Food]  # TODO: genereate the list of food

    def __init__(self) -> None:
        """
        Initialize a game that has a display screen and game actors.
        """

        self._running = False
        self._level = 0  # Current level that the game is in
        self.screen = None
        self.player = None  # TODO: fill out the constructor's parameters appropriately
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

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        self.screen = pygame.display.set_mode \
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.Event) -> None:
        """
        React to the given <event> as appropriate.
        """

        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            self.player.register_event(event.key)

    def on_loop(self) -> None:
        """
        Move all actors in the game as appropriate.
        Check for win/lose conditions and stop the game if necessary.
        """

        self.keys_pressed = pygame.key.get_pressed()
        for actor in self.ghosts:
            actor.chase_pacman(self.player)

        if self.player is None:
            print("You did not make POSt, better luck next time!")
            self._running = False

        elif self.game_won() is True:
            print("Congratulations, you made POSt!")
            self._running = False


    def set_player(self, player: Pacman) -> None:
        """
        Set the game's player to be the given Pacman object.
        """

        self.player = player

    def add_ghost(self, g: Ghost):
        """
        Add a ghost object to the list attribute ghosts
        """
        self.ghosts.append(g)

    def add_food(self, f: Food):
        """
        Add a food object to the list attribute foods
        """
        self.foods.append(f)

    def add_barrier(self, b: Barrier):
        """
        Add a barrier object to the list attribute barriers
        """
        self.barriers.append(b)

    def remove_food(self, f:Food):
        """
        remove a food object once the player has eaten it.
        """
        self.foods.remove(f)

    def is_game_over(self) -> bool:
        """
        Determines if the game is over, which occurs if pacman is caught
        or the goal_CGPA is met.
        """
        if (self.current_CGPA >= self.goal_CGPA):
            if(self.game_won()):
                return True

        for ghost in self.ghosts:
            if (ghost.is_touching(self.player)):
                return True

        return False

    def game_over(self) -> None:
        """
        Set the game as over (remove the player from the game).
        """
        self.player = None

    def closegame(self) -> None:
        """
        close the game.
        """
        pygame.quit()

    def game_won(self) -> bool:
        """
        Return True iff the game has been won, according to the current level.
        """
        if self.foods == [] and self.current_CGPA > 3.0:
            return True
        return False


    def setup_level(self):
        w = len(MAP[0])
        h = len(
            MAP) + 1  # We add a bit of space for the text at the bottom
        self.barriers = []
        self.ghosts = []
        self.foods = []
        self.stage_width, self._stage_height = w, h-1
        self.size = (w*ICON_SIZE, h*ICON_SIZE)

        for i in range(len(MAP)):
            for j in range(len(MAP[i])):
                key = MAP[i][j]
                if key == 'P':
                    self.set_player(Pacman(i,j,24,24,{}))
                elif key == 'G':
                    self.add_ghost(Ghost(i,j,24,24,{}))
                elif key == 'O':
                    self.add_food(Food(i,j,10,10,{}))
                elif key == 'X':
                    self.add_barrier(Barrier(i,j,24,24,{}))

        self.goal_CGPA = 3.0
        self.current_CGPA = 0.0
        self.goal_message = "Objective: Collect good marks to meet your CGPA!"
    
    def on_render(self) -> None:
        """
        Render all the game's elements onto the screen.
        """

        self.screen.fill(BLACK)
        for a in self._actors:
            rect = pygame.Rect(a.x * ICON_SIZE, a.y * ICON_SIZE, ICON_SIZE, ICON_SIZE)
            self.screen.blit(a.icon, rect)

        font = pygame.font.Font('freesansbold.ttf', 12)
        text = font.render(self.goal_message, True, WHITE, BLACK)
        textRect = text.get_rect()
        textRect.center = (self.stage_width * ICON_SIZE // 2, \
                           (self.stage_height + 0.5) * ICON_SIZE)
        self.screen.blit(text, textRect)

        pygame.display.flip()

    def execute(self) -> None:
        """
        Holds the main game loop of the game, which performs actions
        such as checking for user input, making the ghosts chase pacman, etc.
        on a continuous basis. Runs until is_game_over() returns true.
        """
        pygame.init()

        while (not self.is_game_over()):

            # Handle user input. Arrow keys control the player's movement.
            for event in pygame.event.get():
                if (event.key == pygame.K_LEFT):
                    self.player.move_left(self.barriers)
                elif (event.key == pygame.K_RIGHT):
                    self.player.move_right(self.barriers)
                elif (event.key == pygame.K_UP):
                    self.player.move_up(self.barriers)
                elif (event.key == pygame.K_DOWN):
                    self.player.move_down(self.barriers)

            # Make all of the ghosts chase pacman and checks if one of them has caught pacman
            for ghost in self.ghosts:
                ghost.chase_pacman(self.player)
                if (ghost.is_touching(self.player)):
                    is_game_over = True

            # Add to score whenever pacman eats a piece of food
            for food in self.foods:
                if (food.is_touching(self.player)):
                    self.current_CGPA += food.value
