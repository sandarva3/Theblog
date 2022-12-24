import tkinter as tk
import random

# Create the main window
root = tk.Tk()

# Create a canvas to draw on
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a ball that moves across the screen
ball = canvas.create_oval(10, 10, 30, 30, fill="red")
dx = 5
dy = 5

# Create a function to move the ball
def move_ball():
    # Get the current position of the ball
    x1, y1, x2, y2 = canvas.coords(ball)

    # Check if the ball has reached the edge of the canvas
    if x2 > 400:
        dx = -5
    elif x1 < 0:
        dx = 5

    if y2 > 400:
        dy = -5
    elif y1 < 0:
        dy = 5

    # Move the ball
    canvas.move(ball, dx, dy)

    # Call this function again after 5 milliseconds
    root.after(5, move_ball)

# Start the game by calling the move_ball function
move_ball()

# Create a function to handle mouse events
def mouse_event(event):
    # Check if the mouse cursor is inside the ball
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        # If so, change the direction of the ball
        global dx, dy
        dx = -dx
        dy = -dy

# Bind the mouse_event function to left mouse button clicks
canvas.bind("<Button-1>", mouse_event)

# Start the main event loop
root.mainloop()
