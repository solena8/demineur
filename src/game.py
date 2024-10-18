from grid import Grid


class Game:
    def __init__(self, rows: int, columns: int, bombs: int):
        self.game_over: bool = False
        self.game_grid = Grid(rows, columns, bombs)

    def ask_row(self) -> int:
        # demander au joueur de choisir une rangée
        row: str = input("Choisissez une rangée : ")
        # on enlève 1 à l'input pour que ça corresponde à l'index visuellement
        return int(row) - 1

    def ask_column(self) -> int:
        # demander au joueur de choisir une colonne
        column: str = input("Choisissez une colonne : ")
        # on enlève 1 à l'input pour que ça corresponde à l'index visuellement
        return int(column) - 1

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
