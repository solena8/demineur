from grid import Grid
from cell import Cell
from unittest.mock import patch
from game import Game


def test_init_game():
    game = Game(2, 2, 0)
    assert game.rows == 2
    assert game.columns == 2
    assert type(game.game_grid) == Grid
    assert game.game_over == False


def test_ask_row():
    game = Game(10, 10, 10)
    with patch('builtins.input', return_value='5'):
        result = game.ask_row()
        assert result == 4
    with patch('builtins.input', return_value='1'):
        result = game.ask_row()
        assert result == 0

def test_ask_column():
    game = Game(10, 10, 10)
    with patch('builtins.input', return_value='5'):
        result = game.ask_column()
        assert result == 4
    with patch('builtins.input', return_value='1'):
        result = game.ask_column()
        assert result == 0

def test_game_won():
    game = Game(2, 2, 0)
    for r in range(game.rows):
        for c in range(game.columns):
            cell = game.game_grid.grid[r][c]
            cell.hidden = False
    game.game_grid.grid[0][0].hidden = True
    assert game.game_won() == False
    game.game_grid.grid[0][0].bomb = True
    assert game.game_won() == True



