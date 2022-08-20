import turtle

# the coordinates
# of each corner
shape = ((0, 0), (10, 25), (20, 0), (10, -7))

# registering the new shape
turtle.register_shape('diamond', shape)

screen = turtle.Screen()
screen.bgcolor('blue')

gary = turtle.Turtle()
gary.shape("diamond")
gary.color('red')

timer = 0
size = 20


def start_timer():
    global timer, gary, size
    timer += 1
    gary.stamp()
    size = size + 1
    gary.forward(size)
    gary.right(25)
    if timer >= 60: # 60 seconds
        return
    screen.ontimer(start_timer, 1000) # 1 second


start_timer()

screen.mainloop()
