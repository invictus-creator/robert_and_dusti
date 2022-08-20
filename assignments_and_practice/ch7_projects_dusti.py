import math
import random
import turtle
import typing

"""
1. Define a function drawCircle. This function should expect a Turtle object,
the coordinates of the circle’s center point, and the circle’s radius as arguments. 
The function should draw the specified circle. The algorithm should
draw the circle’s circumference by turning 3 degrees and moving a given
distance 120 times. Calculate the distance moved with the formula 2.0 * p *
radius / 120.0
"""


def draw_circle(turtle: turtle.Turtle, center: typing.Union[list, tuple], radius: int):
    """Draws a circle"""
    turn_degrees = 3
    move_count = 120
    distance = 2 * math.pi * radius / move_count
    x, y = center

    turtle.up()
    turtle.goto(x, y)
    turtle.forward(radius)
    turtle.left(90)
    turtle.down()

    for move in range(move_count):
        turtle.forward(distance)
        turtle.left(turn_degrees)


"""
2. Modify this chapter’s case study program (the c-curve) so that it draws the line
segments using random colors.
"""


def cCurve(t: turtle.Turtle, x1, y1, x2, y2, level):
    """Draws a c-curve of the given level."""

    def drawLine(x1, y1, x2, y2):
        """Draws a line segment between the endpoints."""
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    if level == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)


"""
3. The Koch snowflake is a fractal shape. At level 0, the shape is an equilateral triangle. 
At level 1, each line segment is split into four equal parts, producing an
equilateral bump in the middle of each segment. Figure 7-15 shows these shapes
at levels 0, 1, and 2.
    At the top level, the script uses a function drawFractalLine to draw three fractal
lines. Each line is specified by a given distance, direction (angle), and level. The
initial angles are 0, -120, and 120 degrees. The initial distance can be any size,
such as 200 pixels. The function drawFractalLine is recursive. If the level is 0,
then the turtle moves the given distance in the given direction. Otherwise, the
function draws four fractal lines with one-third of the given distance, angles that
produce the given effect, and the given level minus 1. Write a script that draws
the Koch snowflake.
"""


def koch_snowflake():
    """Draws a snowflake"""
    def draw_fractal_line(distance, direction, level):
        """Draws fractal line"""



if __name__ == '__main__':
    print("Which function would you like to call:")
    print("1. draw_circle()")
    print("2. cCurve()")

    function = input("\n> ")

    if function == '1':
        print("\nEnter the center point")
        x = int(input("x pos: "))
        y = int(input("y pos: "))
        center = (x, y)
        print("\nEnter the radius")
        radius = int(input("radius: "))
        t = turtle.Turtle()
        draw_circle(t, center, radius)
        turtle.done()

    elif function == '2':
        level = int(input("\nEnter the level (0 or greater): "))
        if level > 8:
            turtle.tracer(False)
        r, g, b = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t = turtle.Turtle()
        t.pencolor(r, g, b)
        t.hideturtle()
        cCurve(t, 50, -50, 50, 50, level)
        if level > 8:
            turtle.update()
        turtle.done()
