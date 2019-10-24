class Food(Actor):
    value = 0
    
    def __init__(self, start_xpos: float, start_ypos: float):
        super().__init__(start_xpos, start_ypos, 0, {})