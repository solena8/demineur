from grid import Grid

class Game:
    def __init__(self, rows: int, columns: int, bombs: int):
        self.game_over: bool = False
        self.game_grid = Grid(rows, columns, bombs)
        self.rows = rows
        self.columns = columns

    def ask_row(self) -> int:
        row: str = input("Choisissez une rangée : ")
        return int(row) - 1

    def ask_column(self) -> int:
        column: str = input("Choisissez une colonne : ")
        return int(column) - 1

    def game_won(self) -> bool:
        for r in range(self.rows):
            for c in range(self.columns):
                cell = self.game_grid.grid[r][c]
                if cell.hidden and not cell.bomb:
                    return False
        return True

    def game_play(self):
        self.game_grid.print_grid()
        while not self.game_over:
            is_bomb: bool = self.game_grid.is_it_bomb(self.ask_row(), self.ask_column())
            self.game_grid.print_grid()
            if is_bomb:
                self.game_over = True
                print("GAME OVER")
                return
            if self.game_won():
                print("Bravo, vous avez gagné !")
                return