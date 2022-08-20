import turtle
turtle_run = turtle.Screen()
turtle_run.bgcolor("grey")
_turtle = turtle.Turtle()
_turtle.shape("arrow")
_turtle.color("red")

_turtle.penup()
size = 20
for i in range(20):
    _turtle.stamp()             # leave an impression on the canvas
    size = size + 3             # increase the size on every iteration
    _turtle.forward(size)       # move frogger along
    _turtle.right(24)           # ... and turn her
    turtle.ontimer(_turtle, t=400 * (i + 1))
turtle_run.mainloop()