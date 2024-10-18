from cell import Cell

def test_init_cell():
    cell = Cell()
    assert cell.hidden == True
    assert cell.bomb == False
    assert cell.hint == 0

def test_display_hidden():
    cell = Cell()
    assert cell.display() == "⬛"

def test_display_bomb():
    cell = Cell()
    cell.hidden = False
    cell.bomb = True
    assert cell.display() == "💣"

def test_reveal():
    cell = Cell()
    assert cell.hidden == True
    cell.reveal()
    assert cell.hidden == False