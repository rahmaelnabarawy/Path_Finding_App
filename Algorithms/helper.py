from config import *

def get_neighbors(grid, cell):
    neighbors = []
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = cell.row + d[0], cell.col + d[1]
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c].color != "black":
            neighbors.append(grid[r][c])
    return neighbors
