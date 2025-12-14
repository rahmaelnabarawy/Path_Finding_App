import tkinter as tk
from UI.visualizer import *

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pathfinding Visualizer")
    app = Visualizer(root)
    root.mainloop()
