from config import *

def show_overlay_message(self, message, color="black", duration=2000):
    # Calculate center of canvas
    center_x = (COLS * CELL_SIZE) // 2
    center_y = (ROWS * CELL_SIZE) // 2
    
    # Create semi-transparent background rectangle
    self.canvas.create_rectangle(
        center_x - 200, center_y - 50,
        center_x + 200, center_y + 50,
        fill="white",
        outline="black",
        width=3,
        tags="overlay"
    )
    
    # Create text
    self.canvas.create_text(
        center_x, center_y,
        text=message,
        font=("Arial", 24, "bold"),
        fill=color,
        tags="overlay"
    )
    
    # Auto-remove after duration (if not permanent)
    if duration > 0:
        self.root.after(duration, lambda: self.canvas.delete("overlay"))

def show_running_overlay(self):
    center_x = (COLS * CELL_SIZE) // 2
    center_y = (ROWS * CELL_SIZE) // 2
    
    # Semi-transparent background
    self.canvas.create_rectangle(
        center_x - 150, center_y - 40,
        center_x + 150, center_y + 40,
        fill="lightblue",
        outline="blue",
        width=2,
        tags="running_overlay"
    )
    
    # Running text
    self.canvas.create_text(
        center_x, center_y,
        text="Searching for path...",
        font=("Arial", 16, "italic"),
        fill="darkblue",
        tags="running_overlay"
    )

def remove_running_overlay(self):
    self.canvas.delete("running_overlay")