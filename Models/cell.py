class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = "white"

    def make_start(self):
        self.color = "green"

    def make_end(self):
        self.color = "red"

    def make_wall(self):
        self.color = "black"

    def make_path(self):
        self.color = "yellow"
