import time
from queue import PriorityQueue
from config import *
from Models.cell import *
from Models.node import *
from Algorithms.helper import get_neighbors

def heuristic(cell):
    return abs(cell.row - end_cell.row) + abs(cell.col - end_cell.col)

def a_star(draw, grid, start, end):
    global end_cell
    end_cell = end
    count = 0
    start_time = time.perf_counter()
    expanded_nodes = 0

    q = PriorityQueue()
    visited = set() 
    
    start_node = Node(cell=start, path=[start])
    visited.add((start.row, start.col))
    
    q.put((heuristic(start), 0, count, start_node))

    while not q.empty():
        h, g, _, node = q.get()
        expanded_nodes += 1
        current_cell = node.cell

       
        if current_cell != start and current_cell != end:
            current_cell.make_visited()
        draw()

       
        if current_cell == end:
            for cell in node.path:
                if cell != start and cell != end:
                    cell.make_path()
                    draw()
            end_time = time.perf_counter()
            return {
                "found": True,
                "time_ms": (end_time - start_time) * 1000,
                "expanded_nodes": expanded_nodes,
                "path_length": len(node.path)
            }

     
        neighbors = get_neighbors(grid, current_cell)
        for n in neighbors:
            neighbor_pos = (n.row, n.col)
            
            if neighbor_pos not in visited:  
                visited.add(neighbor_pos)
                
                if n != start and n != end:
                    n.make_visited()
                
                count += 1
                neighbor_path = node.path + [n]
                neighbor = Node(n, neighbor_path)
                new_g = g + 1
                h_new = new_g + heuristic(n)
                q.put((h_new, new_g, count, neighbor))

    end_time = time.perf_counter()
    return {
        "found": False,
        "time_ms": (end_time - start_time) * 1000,
        "expanded_nodes": expanded_nodes,
        "path_length": 0
    }