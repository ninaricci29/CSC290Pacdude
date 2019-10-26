class Food(Actor):
    value = 0
    
    def __init__(self, start_xpos: float, start_ypos: float, width: float, height: float, sprite):
        super().__init__(start_xpos, start_ypos, width, height, 0, sprite)