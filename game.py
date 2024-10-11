from grid import Grid


class Game:

    def __init__(self, rows: int, columns: int, bombs: int):
        # la classe Game a 3 attributs : grid, une instanciation de Grid
        # self.hiding_grid qui représente la grille telle que le joueur la voit
        # self.hidden_grid qui représente la grille cachée en dessous
        self.grid: Grid = Grid(rows, columns, bombs)
        self.hiding_grid: list = [self.grid.visual_hidden_case] * (rows * columns)
        self.hidden_grid: list = self.grid.generate_hidden_grid()

    def pick_case(self, show_case_index: int):
        grid_size: int = self.grid.rows * self.grid.columns  # Taille totale de la grille
        if 0 <= show_case_index < grid_size:
            # On remplace la case dans la hiding_grid par celle de hidden_grid
            self.hiding_grid[show_case_index] = self.hidden_grid[show_case_index]
        else:
            print(f"Please pick a number between 0 and {grid_size - 1}")

    def print_grid(self):
        for i in range(self.grid.rows):
            # Découpe la liste en lignes de la longueur des colonnes pour afficher une grille
            row = self.hiding_grid[i * self.grid.columns:(i + 1) * self.grid.columns]
            print(" ".join(row))
