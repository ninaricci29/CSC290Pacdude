import Actor, Pacman, Food, Barrier

#global variables
RES_WIDTH = 50
RES_HEIGHT = 50
points = 0
pacman = Pacman(0, 0)

#func


def is_game_over():
    pass


#main game loop
while (not is_game_over()):
    for food in foods:
        if pacman.is_touching(food):
            points += 1
