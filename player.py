

class Pacman(Actor):
    """
    A class to represent a Player in the game.
    """
    # === Private Attributes ===
    # _CGPA_collected:
    #       the cgpa the player has earned so far
    # _last_event:
    #       keep track of the last key the user pushed down
    # _smooth_move:
    #       represent on/off status for smooth player movement

    x: int
    y: int
    icon: pygame.Surface
    _CGPA_collected: float
    _last_event: Optional[int]
    _smooth_move: bool
    _num_lives : int

        
    def __init__(self, icon: str, x: int, y: int) -> None:
        """Initalize a Player with the given image <icon> at the position
        <x> and <y> on the stage."""

        super().__init__(icon_file, x, y)
        self._CGPA_collected = 0
        self._num_lives = 3
    
    def is_dead(self) -> bool:
        """
        Return True if the Player is not alive.
        """
        
        return False

    def move(self, game: 'Game') -> None:
        """
        Move the player on the <game>'s stage based on keypresses.
        """

        evt = self._last_event
        if self._last_event:
            dx, dy = 0, 0
            if self._smooth_move:  # Smooth movement
                if game.keys_pressed[pygame.K_LEFT] or game.keys_pressed[pygame.K_a]:
                    dx -= 1
                elif game.keys_pressed[pygame.K_RIGHT] or game.keys_pressed[pygame.K_d]:
                    dx += 1
                elif game.keys_pressed[pygame.K_UP] or game.keys_pressed[pygame.K_w]:
                    dy -= 1
                elif game.keys_pressed[pygame.K_DOWN] or game.keys_pressed[pygame.K_s]:
                    dy += 1

            else:  # Precise movement
                if evt == pygame.K_LEFT or evt == pygame.K_a:
                    dx -= 1
                if evt == pygame.K_RIGHT or evt == pygame.K_d:
                    dx += 1
                if evt == pygame.K_UP or evt == pygame.K_w:
                    dy -= 1
                if evt == pygame.K_DOWN or evt == pygame.K_s:
                    dy += 1
                self._last_event = None

            new_x, new_y = self.x + dx, self.y + dy
            name_actor = game.get_actor(new_x, new_y)
            # i.e. Check if move is possible / if star is to be collected, etc.

            if (dx, dy) != (0, 0):

                # increase the cgpa of the player if they eat a point
                if isinstance(name_actor, Food):
                    self._CGPA_collected += name_actor.getValue()
                    game.remove_actor(name_actor)
                    self.x, self.y = new_x, new_y

                # move the player as long as they are not trying to go into a wall
                elif (not isinstance(name_actor, Barrier):
                    self.x, self.y = new_x, new_y
                
                # if the player touches a ghost, they lose a life, and game over if all lives are depleted
                elif isinstance(name_actor, Ghost):
                      self._num_lives =- 1
                      if self._num_lives == 0:
                        self.is_dead = True
                        game.remove_actor(self)       
                        self.is_game_over = True
                      #Game Over -exit game loop
                      else:
                         #Reset PacMan and Ghosts back to their original spots, but keep the cgpa points where they are
                         #Start the game again
                      
