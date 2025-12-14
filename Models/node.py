class Node:
    def __init__(self, cell, path):
        self.cell = cell
        self.path = path

    def __repr__(self):
        return '->'.join([f'({c.row},{c.col})' for c in self.path])
