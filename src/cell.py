class Cell:
    BOMB_VISUAL = "💣"

    def __init__(self):
        self.hidden = True
        self.bomb = False
        self.hint = 0

    def display(self) -> str:
        # Affiche soit la cellule cachée, soit son contenu si révélé.
        if self.hidden:
            return "⬛"
        else:
            if self.bomb:
                return self.BOMB_VISUAL
            else:
                if self.hint > 0:
                    return str(self.hint)+" "
                else:
                    return "* "

    def reveal(self):
        """Révéler la cellule."""
        self.hidden = False
