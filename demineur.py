# Etape 1
# Pour commencer, avant de pouvoir poser nos bombes, il nous faut une grille et par conséquent une fonction génératrice de grille.
#
import random

from six import print_


def generate_grid(M, N):
    # creation d'une liste vide
    grid: list = []
    # pour chaque rangée selon le nb M, création d'une liste row
    for x in range(M):
        row: list = []
        # pour chaque élément de row, on ajoute un 0 dedans selon le nb N
        for y in range(N):
            row.append("⬛")
        # maintenant on ajoute chaque rangée à la liste grid
        grid.append(row)
    # on retourne la liste (de taille M) de listes (toutes de taille N)
    return grid

def print_grid(grid):
    # pour chaque petite liste de la liste parent, on joint les éléments
    # on les sépare avec un | et on print la liste
    # ainsi chaque rangée apparait en dessoous de la précédente, créant une grille visuelle
    for row in grid:
        print(" | ".join(row))

grid = generate_grid(3, 3)

# print_grid(grid)

# Notre générateur de grille pourrait, à partir d'une taille de côté M - ou 2 tailles (M,N) pour une
# grille rectangulaire -, générer une superbe grille. Remplie de 0 par exemple pour simplifier le coté "vide".
# Et qui pourrait, à partir d'un entier K, générer une grille (superbe rappelons-le) parsemée de K merveilleuses cases pleines
# (ou noires, ou True, ou X) dans un océan de M*N-K cases vides (ou blanches, ou False). Ces K cases pleines seraient,
# réparties aléatoirement sur la grille.
# Générer cette grille en ligne de commande en python.

def generate_mixed_grid(M, N, K):
    # creation d'une liste vide
    grid: list = []
    # création d'une liste contenant toutes les cases qu'on va utiliser pour piocher ensuite une bombe ou un espace vide
    # au hasard pour former la grille finale (liste de K bombes et le reste (M*N - K) vides
    selection_grid: list = (["💣"] * K) + (["  "] * (M * N - K))
    for x in range(M):
        row: list = []
        # pour chaque élément de row, on ajoute un élément de la sélection au hasard selon le nb N
        for y in range(N):
            grid_item = random.choice(selection_grid)
            row.append(grid_item)
            # on supprime l'élément de la liste de sélection en cherchant son index dans la liste
            selection_grid.pop(selection_grid.index(grid_item))
        grid.append(row)
    return grid

grid_2 = generate_mixed_grid(10, 10, 28)

# print_grid(grid_2)



# Etape 2 - Cachez cette grille que je ne saurais voir !
# Mais imaginez, si la grille était d'abord neutre, et que vous puissiez, les une après les autres, sélectionner les cases
# (par exemple en renseignant leurs coordonnées en ligne de commande), et les découvrir : soit pleines (ou noires, ou True),
# soit vides (ou blanches, ou False) ?

# Il vous faut pour cela une logique en boucle :

# La grille est affichée dans un certain état A. Au début, cette état est "neutre" : on ne connait pas le contenu des cases.
# Le jeu attend une action, un ordre ; vous l'exécutez (vous renseignez des coordonnées par exemple, ou - si vous vous êtes
# déjà diversifié dans le graphisme - vous cliquer sur une case, ...).
# Le jeu vous affiche le nouvel état B de la grille (l'état A plus le résultat de votre action).
# On recommence la boucle avec ce nouvel état B.

rows:int = 10
columns:int = 10
nb_of_bombs:int =30
neutral_grid: list = generate_grid(rows, columns)
real_grid: list = generate_mixed_grid(rows, columns, nb_of_bombs)

def pick_case(index_nb, empty_grid, full_grid)-> list:
    single_list_empty_grid = [item for row in empty_grid for item in row]
    single_list_full_grid = [item for row in full_grid for item in row]
    single_list_empty_grid[index_nb] = single_list_full_grid[index_nb]
    return single_list_empty_grid

def print_grid_2(single_list_empty_grid, M, N):
    for i in range(M):
        # sépare la liste en 10 par 10 pour afficher en grille
        row = single_list_empty_grid[i*N:(i+1)*N]
        print(" ".join(row))

grid_2 = pick_case(5, neutral_grid, real_grid)

print_grid_2(grid_2, rows, columns)

grid_3 = pick_case(54, grid_2, real_grid)

print("     ")

print_grid_2(grid_3, rows, columns)

