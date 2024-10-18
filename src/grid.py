import random
from cell import Cell

class Grid:
    def __init__(self, rows: int, columns: int, bombs: int):
        self.rows: int = rows
        self.columns: int = columns
        self.bombs : int = bombs
        self.grid: list[list[Cell]] = self.generate_grid()

    def generate_grid(self) -> list[list[Cell]]:
        cells: list = []
        # Ajout des cellules avec bombes
        for _ in range(self.bombs):
            cell = Cell()
            cell.bomb = True  # Marquer cette cellule comme une bombe
            cells.append(cell)
        # Ajout des cellules sans bombes
        for _ in range(self.rows * self.columns - self.bombs):
            cells.append(Cell())
        random.shuffle(cells)  # Mélange des cases
        # Transforme la liste en grille 2D
        grid_2d = [cells[i * self.columns:(i + 1) * self.columns] for i in range(self.rows)]
        return grid_2d

    def count_bombs_around(self, row: int, col: int) -> int:
        # Compte le nombre de bombes autour d'une cellule spécifique.
        bombs_count = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (0 <= r < self.rows and 0 <= c < self.columns) and not (r == row and c == col):
                    if self.grid[r][c].bomb:
                        bombs_count += 1
        return bombs_count


    def is_it_bomb(self, row: int, col: int) -> bool:
        # Révèle une cellule spécifique.
        cell: Cell = self.grid[row][col]
        if cell.hidden:
            cell.reveal()  # Marquer la cellule comme révélée
            if cell.bomb:
               return True
            else:
                # Si c'est une cellule sans bombe, mettre à jour avec le nombre de bombes autour
                bombs_around = self.count_bombs_around(row, col)
                if bombs_around > 0:
                    # On met à jour le contenu de la cellule avec le nombre de bombes autour
                    cell.hint = bombs_around
            self.recursive_reveal(row, col)
        return False

    def recursive_reveal(self, row: int, col: int):
        # On parcourt les 8 cases autours de celle choisie
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                # Vérification des limites de la grille
                if 0 <= r < self.rows and 0 <= c < self.columns:
                    cell = self.grid[r][c]
                    # Si ce n'est pas une bombe et que la cellule est cachée
                    if not cell.bomb and cell.hidden:
                        # On révèle la cellule et on calcule son indice
                        cell.hint = self.count_bombs_around(r, c)
                        cell.reveal()
                        # Si l'indice est 0, on continue la révélation récursive
                        if cell.hint == 0:
                            self.recursive_reveal(r, c)



    def print_grid(self):
        # Affiche la grille avec les cases cachées/révélées.
        for row in self.grid:
            display_row = [cell.display() for cell in row]
            print(" ".join(display_row))


