class Food(Actor):
    """
    A piece of food that pacman can eat to gain points or powerups.
    """
    
    value = 0
    def __init__(self, start_xpos: float, start_ypos: float, \
                 width: float, height: float, sprite, value):
        super().__init__(start_xpos, start_ypos, width, height, 0, sprite)
        self.value = value