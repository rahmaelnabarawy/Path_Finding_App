from queue import PriorityQueue
from config import *
from Models.cell import *
from Models.node import *

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

def a_star(draw, grid, start, end):
    global end_cell
    end_cell = end

    open_set = PriorityQueue()
    start_node = Node(start, [start])
    open_set.put((heuristic(start), 0, 0, start_node))  # (f_score, g_score, counter, node)
    count = 0

    while not open_set.empty():
        f_score, g_score, _, current_node = open_set.get()
        current_cell = current_node.cell

        if current_cell == end:
            # Draw the path
            for c in current_node.path:
                if c != start and c != end:
                    c.make_path()
                draw()
            return True

        for neighbor in get_neighbors(grid, current_cell):
            if neighbor not in current_node.path:  # avoid cycles
                new_path = current_node.path + [neighbor]
                new_g = g_score + 1
                new_f = new_g + heuristic(neighbor)
                count += 1
                open_set.put((new_f, new_g, count, Node(neighbor, new_path)))

        draw()

    return False
