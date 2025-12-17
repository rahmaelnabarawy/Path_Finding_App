import time
from collections import deque
from Algorithms.helper import get_neighbors
from config import *
from Models.cell import *
from Models.node import *

def bfs(draw, grid, start, end):
    start_time = time.perf_counter()
    expanded_nodes = 0

    queue = deque()
    start_node = Node(start, [start])
    queue.append(start_node)
    
    visited = set()
    visited.add((start.row, start.col))

    while queue:
        current_node = queue.popleft()
        expanded_nodes += 1

        current_cell = current_node.cell

        if current_cell != start and current_cell != end:
            current_cell.make_visited()
        draw()

        if current_cell == end:
            for c in current_node.path:
                if c != start and c != end:
                    c.make_path()
                draw()

            end_time = time.perf_counter()
            return {
                "found": True,
                "time_ms": (end_time - start_time) * 1000,
                "expanded_nodes": expanded_nodes,
                "path_length": len(current_node.path)
            }

        for neighbor in get_neighbors(grid, current_cell):
            neighbor_pos = (neighbor.row, neighbor.col)
            if neighbor_pos not in visited:
                visited.add(neighbor_pos)
                new_path = current_node.path + [neighbor]
                queue.append(Node(neighbor, new_path))

    end_time = time.perf_counter()
    return {
        "found": False,
        "time_ms": (end_time - start_time) * 1000,
        "expanded_nodes": expanded_nodes,
        "path_length": 0
    }
