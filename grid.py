import random

class Grid:

    def __init__(self, rows, columns, bombs):
        # la classe Grid a 7 attributs :
        # self.rows qui correspond au nombre de rangs
        # self.columns qui correspond au nombre de colonnes
        # self.bombs qui correspond au nombre de bombes insérées
        # self.empty_case qui correspond au nombre de cases vides
        # self.visual_bomb qui correspond à la représentation visuelle des bombes
        # self.visual_empty_case: qui correspond à la représentation visuelle des cases vides
        # self.visual_hidden_case:  qui correspond à la représentation visuelle des cases encore cachées
        self.rows: int = rows
        self.columns: int = columns
        self.bombs: int = bombs
        self.empty_case: int = rows * columns - bombs
        self.visual_bomb: str = "💣"
        self.visual_empty_case: str = " "
        self.visual_hidden_case: str = "⬛"

    def generate_hidden_grid(self) -> list:
        # on crée une liste avec autant de bombes et cases vides que demandé
        selection_grid = [self.visual_bomb] * self.bombs + [
            self.visual_empty_case] * self.empty_case
        random.shuffle(selection_grid)  # on mélange aléatoirement les bombes et les cases vides
        return selection_grid


