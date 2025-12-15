from queue import PriorityQueue
from config import *
from Models.cell import *
from Models.node import *
from Algorithms.helper import *

# --- Heuristic for grid (Manhattan distance)
def heuristic(cell):
    return abs(cell.row - end_cell.row) + abs(cell.col - end_cell.col)

def a_star(draw,grid,start,end):
    global end_cell
    end_cell = end
    count=0 ##randum value
    q=PriorityQueue()
    start_node=Node(cell=start,path=[start])
    
    q.put((heuristic(start),0,count,start_node))
    while not q.empty():
        
        h,g,randum_val,node=q.get()
        if node.cell== end:
            for cell in node.path:
                if cell!=start and cell !=end:
                    cell.make_path()
                    draw()
            return  True            
        else:
            neighbors=get_neighbors(grid ,node.cell)
            for n in neighbors:
             if n not in node.path:
                if n !=start and n!=end:
                    n.make_visited()
                count=count+1
                neighbor_path=node.path+[n]
                neighbor=Node(n,neighbor_path)
                new_g=g+1
                h=new_g+heuristic(n)
                
                q.put((h,new_g,count,neighbor))
    return False    
