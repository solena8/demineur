from game import Game

# choix des variables
rows:int = 10
columns: int = 10
bombs: int = 30

# instanciation du jeu 1
game_1= Game(rows, columns, bombs)


# choix de la première case à dévoiler
game_1.pick_case(54)
# impression de la grille après choix
game_1.print_grid()

print("second tour")

# choix de la première case à dévoiler

game_1.pick_case(99)
game_1.print_grid()