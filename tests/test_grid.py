from cell import Cell
from unittest.mock import patch
from io import StringIO
from grid import Grid

def test_init_grid():
    grid = Grid(2, 2, 1)
    assert grid.rows == 2
    assert grid.columns == 2
    assert grid.bombs == 1

def test_generate_grid():
    grid = Grid(2, 2, 1)
    assert len(grid.grid) == 2
    assert len(grid.grid[0]) == 2
    assert len(grid.grid[1]) == 2
    cnt_bomb = 0
    for row in grid.grid:
        for cell in row:
            assert type(cell) == Cell
            if cell.bomb == True:
                cnt_bomb += 1
    assert cnt_bomb == 1

def test_count_bombs_around():
    grid = Grid(3, 3, 0)
    assert grid.count_bombs_around(0, 0) == 0
    assert grid.count_bombs_around(0, 1) == 0
    assert grid.count_bombs_around(0, 2) == 0
    assert grid.count_bombs_around(1, 0) == 0
    assert grid.count_bombs_around(1, 1) == 0
    assert grid.count_bombs_around(1, 2) == 0
    assert grid.count_bombs_around(2, 0) == 0
    assert grid.count_bombs_around(2, 1) == 0
    assert grid.count_bombs_around(2, 2) == 0
    grid.grid[0][0].bomb = True
    assert grid.count_bombs_around(0, 0) == 0
    assert grid.count_bombs_around(0, 1) == 1
    assert grid.count_bombs_around(0, 2) == 0
    assert grid.count_bombs_around(1, 0) == 1
    assert grid.count_bombs_around(1, 1) == 1
    assert grid.count_bombs_around(1, 2) == 0
    assert grid.count_bombs_around(2, 0) == 0
    assert grid.count_bombs_around(2, 1) == 0
    assert grid.count_bombs_around(2, 2) == 0
    grid.grid[1][1].bomb = True
    assert grid.count_bombs_around(0, 0) == 1
    assert grid.count_bombs_around(0, 1) == 2
    assert grid.count_bombs_around(0, 2) == 1
    assert grid.count_bombs_around(1, 0) == 2
    assert grid.count_bombs_around(1, 1) == 1
    assert grid.count_bombs_around(1, 2) == 1
    assert grid.count_bombs_around(2, 0) == 1
    assert grid.count_bombs_around(2, 1) == 1
    assert grid.count_bombs_around(2, 2) == 1

def test_is_it_bomb():
    grid = Grid(3, 3, 0)
    assert grid.grid[1][1].hint == 0
    assert grid.grid[1][2].hidden == True
    grid.grid[0][0].bomb = True
    grid.is_it_bomb(1, 2)
    assert grid.grid[1][1].hint == 1
    assert grid.grid[2][2].hint == 0
    assert grid.is_it_bomb(0, 0) == True
    assert grid.is_it_bomb(1, 2) == False
    assert grid.is_it_bomb(2, 1) == False
    assert grid.grid[1][2].hidden == False


def test_print_grid():
    grid = Grid(2, 2, 0)
    grid.grid[0][0].hidden = False
    grid.grid[0][0].hint = 1
    grid.grid[0][1].hidden = False
    grid.grid[0][1].bomb = True
    grid.grid[1][1].hidden = False
    grid.grid[1][1].hint = 0
    with patch('sys.stdout', new=StringIO()) as fake_out:
        grid.print_grid()
        output = fake_out.getvalue().strip()
    expected_output = "1 💣\n⬛ *"
    assert output == expected_output

