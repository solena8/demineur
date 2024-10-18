from grid import Grid


class Game:
    def __init__(self, rows: int, columns: int, bombs: int):
        self.game_over: bool = False
        self.game_grid = Grid(rows, columns, bombs)

    def ask_row(self) -> int:
        # demander au joueur de choisir une rangée
        row: str = input(f"Choisissez une rangée (entre 1 et {self.game_grid.rows}) : ")
        # vérifier si l'entrée est un nombre
        while not row.isdigit() or not (1 <= int(row) <= self.game_grid.rows):
            print(f"Merci de choisir un nombre entre 1 et {self.game_grid.rows}.")
            row = input(f"Choisissez une rangée (entre 1 et {self.game_grid.rows}) : ")
        return int(row) - 1  # On soustrait 1 pour correspondre à l'index1

    def ask_column(self) -> int:
        # demander au joueur de choisir une colonne
        column: str = input(f"Choisissez une colonne (entre 1 et {self.game_grid.columns}) : ")
        # vérifier si l'entrée est un nombre
        while not column.isdigit() or not (1 <= int(column) <= self.game_grid.columns):
            print(f"Merci de choisir un nombre entre 1 et {self.game_grid.columns}.")
            column = input(f"Choisissez une rangée (entre 1 et {self.game_grid.columns}) : ")
        return int(column) - 1  # On soustrait 1 pour correspondre à l'index1

    def game_won(self) -> bool:
        # S'il ne reste aucune case cahée qui ne soit pas une bombe, c'est gagné
        for r in range(self.game_grid.rows):
            for c in range(self.game_grid.columns):
                cell = self.game_grid.grid[r][c]
                if cell.hidden and not cell.bomb:
                    return False
        return True

    def game_play(self):
        # on montre d'abord la grille toute cachée
        self.game_grid.print_grid()
        # tant que la condition game over n'est pas atteinte
        while not self.game_over:
            # on appelle is_bomb qui revele la case choisie, verifie si c'est une bombe et continue en recursif si besoin
            is_bomb: bool = self.game_grid.is_it_bomb(self.ask_row(), self.ask_column())
            # on montre la grille avec les indices obtenus
            self.game_grid.print_grid()
            #  si on est tombé sur une bombe, la méthode retourne True et on perd
            if is_bomb:
                self.game_over = True
                print("GAME OVER")
                return
            # sinon on vérifie si les conditions de victoire sont remplies et si oui c'est gagné !
            if self.game_won():
                print("Bravo, vous avez gagné !")
                return
