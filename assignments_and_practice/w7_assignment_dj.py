import turtle
frogscreen = turtle.Screen()
frogscreen.bgcolor("blue")
frogger = turtle.Turtle()
frogger.shape("turtle")
frogger.color("red")

frogger.penup()
size = 20
for i in range(20):
    frogger.stamp()             # leave an impression on the canvas
    size = size + 3             # increase the size on every iteration
    frogger.forward(size)       # move frogger along
    frogger.right(24)           # ... and turn her

frogscreen.mainloop()