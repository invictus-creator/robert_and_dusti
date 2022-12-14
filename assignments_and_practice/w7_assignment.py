"""
Program: w7_assignment.py
Author: Robert Timberlake
Creates a hexagon pattern with random colors for a minute.
"""
import turtle
import time
import random

# Create a function for hexagon
def hexagon(t, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)


# Define turtle attributes
turtle_app = turtle.Screen()
turtle_app.bgcolor("grey")
_turtle = turtle.Turtle()
_turtle.shape("arrow")
_turtle.speed(10)
turtle.colormode(255)

# Write name on screen
_turtle.penup()
x, y = (turtle_app.window_width() / 3, turtle_app.window_height() / 3)
_turtle.goto(x, y)
_turtle.write("Robert Timberlake", font=('Segue UI', 20, 'bold'))
_turtle.goto(0, 0)
_turtle.pendown()

# Create a one-minute loop that creates a hexagon pattern using random colors
start_time = time.time()
while time.time() - start_time <= 60:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    _turtle.pencolor(r, g, b)
    _turtle.left(93)
    hexagon(_turtle, 100)

turtle.done()
