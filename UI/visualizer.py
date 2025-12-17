from Algorithms import dfs
from Algorithms.a_star import *
from Algorithms.bfs import *
from Algorithms.dfs import *
from Models.cell import *
from UI.status import *
import tkinter as tk

class Visualizer:
    def __init__(self, root):
        self.results = {}
        self.root = root
        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE)
        self.canvas.pack()
        self.grid = [[Cell(r,c) for c in range(COLS)] for r in range(ROWS)]
        self.start = None
        self.end = None
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.left_click)
        self.canvas.bind("<B1-Motion>", self.left_drag)
        self.canvas.bind("<Button-3>", self.right_click)
        self.root.bind("<space>", self.start_astar)  
        self.root.bind("b", self.start_bfs)          
        self.root.bind("d", self.start_dfs)          
        self.root.bind("c", self.clear_grid)

    def draw_grid(self):
        self.canvas.delete("all")
        for row in self.grid:
            for cell in row:
                x1, y1 = cell.col*CELL_SIZE, cell.row*CELL_SIZE
                x2, y2 = x1+CELL_SIZE, y1+CELL_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=cell.color, outline="gray")

    def get_cell(self, event):
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.grid[row][col]
        return None

    def left_click(self, event):
        cell = self.get_cell(event)
        if cell:
            if not self.start:
                self.start = cell
                cell.make_start()
            elif not self.end and cell != self.start:
                self.end = cell
                cell.make_end()
            elif cell != self.start and cell != self.end:
                cell.make_wall()
            self.draw_grid()

    def left_drag(self, event):
        cell = self.get_cell(event)
        if cell and cell != self.start and cell != self.end:
            cell.make_wall()
            self.draw_grid()

    def right_click(self, event):
        cell = self.get_cell(event)
        if cell:
            if cell == self.start:
                self.start = None
            if cell == self.end:
                self.end = None
            cell.color = "white"
            self.draw_grid()

    def start_astar(self, event):
        if self.start and self.end:
            show_running_overlay(self)
            self.root.update()
            res = a_star(self.draw_grid, self.grid, self.start, self.end)
            remove_running_overlay(self)
            if res :
                show_overlay_message(self,"PATH FOUND!", "green", 2000)
            else:
                show_overlay_message(self,"PATH NOT FOUND!", "red", 2000)

    def start_bfs(self, event):
        if self.start and self.end:
            show_running_overlay(self)
            self.root.update()
            result = bfs(self.draw_grid, self.grid, self.start, self.end)
            self.results["BFS"] = result
            if result["found"]:
                show_overlay_message(self, "PATH FOUND!", "green", 2000)
            else:
                show_overlay_message(self, "PATH NOT FOUND!", "red", 2000)

    def start_dfs(self, event):
        if self.start and self.end:
            show_running_overlay(self)
            self.root.update()
            res = dfs(self.draw_grid, self.grid, self.start, self.end)
            remove_running_overlay(self)
            if res :
                show_overlay_message(self,"PATH FOUND!", "green", 2000)
            else:
                show_overlay_message(self,"PATH NOT FOUND!", "red", 2000)

    def clear_grid(self, event):
        self.start = None
        self.end = None
        for row in self.grid:
            for cell in row:
                cell.color = "white"
        self.draw_grid()
