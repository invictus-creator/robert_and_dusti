import random
import time
import turtle

window = turtle.Screen()
window.bgcolor("black")

player = turtle.Turtle()
player.shape("classic")
player.begin_fill()

start = time.time()
while time.time() - start < 60:  # run for 60 secs
    player.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    player.forward(300)
    player.left(230)
    window.update()

player.end_fill()
player.penup()
x, y = (window.window_width() / 3), (window.window_height() / 2.5)
player.goto((x, y))
player.write("Dusti Johnson", True, align="center", font=('Segoe UI', 20, 'bold'))

turtle.done()
