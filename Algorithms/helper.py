from config import *
from Algorithms.a_star import end_cell

# --- Heuristic for grid (Manhattan distance)
def heuristic(cell):
    return abs(cell.row - end_cell.row) + abs(cell.col - end_cell.col)


# --- Get neighbors in 4 directions
def get_neighbors(grid, cell):
    neighbors = []
    for d in [(-1,0),(1,0),(0,-1),(0,1)]:
        r, c = cell.row + d[0], cell.col + d[1]
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c].color != "black":
            neighbors.append(grid[r][c])
    return neighbors
