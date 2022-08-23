import math
import random
import time
import turtle


def rainbow_spiral(rgb, i, pen):
    r, g, b = rgb
    i += 1
    if i < 255 // 3:
        g += 3
    elif i < 255 * 2 // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < 255 * 4 // 3:
        g -= 3
    elif i < 255 * 5 // 3:
        r += 3
    else:
        b -= 3

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0

    pen.forward(40 + i)
    pen.right(89)
    pen.pencolor(r, g, b)
    _rgb = (r, g, b)
    return _rgb, i


# start values for rainbow spiral
r, g, b = 255, 0, 0
i = 0

# start values for diamond geometric design
x = 0
y = 0
y2 = 300
space = 10

window = turtle.Screen()
window.bgcolor("black")  # 1 attr change

pen = turtle.Turtle()
pen.shape("classic")  # 2 attr change
pen.shapesize(2, 6, 2)  # 3 attr change
pen.speed(12)  # 4 attr change
pen.pencolor(r, g, b)  # 5 attr change

make_rainbow = False
center_rainbow = True

start = time.time()
while time.time() - start < 60:  # run for 60 secs
    if make_rainbow:
        if center_rainbow:
            pen.penup()
            pen.goto(-20, 20)
            pen.pendown()
            center_rainbow = False
        (_r, _g, _b), i = rainbow_spiral((r, g, b), i, pen)
        r, g, b = (_r, _g, _b)
    else:
        pen.goto(0, y2)

        if x > 0:
            y2 -= space
        if x < 0:
            y2 += space
            if y2 == 300:
                make_rainbow = True

        if y2 > 0:
            x += space
        if y2 < 0:
            x -= space

        pen.goto(x, y)

pen.penup()
x, y = (window.window_width() / 3), (window.window_height() / 2.5)
pen.goto((x, y))
pen.shapesize(1, 1, 1)
pen.pencolor("white")
pen.write("Dusti Johnson", True, align="center", font=('Segoe UI', 20, 'bold'))

turtle.done()
