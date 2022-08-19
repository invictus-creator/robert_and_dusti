# Turtle Attributes
"""
uses (x,Y) system
origin (0,0) is called home

Heading	- Specified in degrees, the heading or direction increases
        in value as the turtle turns to the left, or
        counterclockwise. Conversely, a negative quantity of
        degrees indicates a right, or clockwise, turn. The turtle
        is initially facing east, or 0 degrees. North is 90
        degrees.
Color	- Initially black, the color can be changed to any of more
        than 16 million other colors.
Width	- This is the width of the line drawn when the turtle
        moves. The initial width is 1 pixel. (You’ll learn more
        about pixels shortly.)
Down	- This attribute, which can be either true or false,
        controls whether the turtle’s pen is up or down. When true
        (that is, when the pen is down), the turtle draws a line when it
        moves. When false (that is, when the pen is up), the turtle
        can move without drawing a line.
"""
# Turtle Methodds
from book_programs.polygons import radialPattern

"""
Turtle Method	        What It Does
t = Turtle()	        Creates a new Turtle object and opens its 
                window.
t.home()	            Moves t to the center of the window and     
                then points t east.
t.up()	                Raises t’s pen from the drawing surface.
t.down()	            Lowers t’s pen to the drawing surface.
t.setheading(degrees)	Points t in the indicated direction, 
                which is specified in degrees. East is 0 degrees, 
                north is 90 degrees, west is 180 degrees, and 
                south is 270 degrees.
t.left(degrees)         Rotates t to the left or the right by the 
t.right(degrees)        specified degrees.
t.goto(x, y)	        Moves t to the specified position.
t.forward(distance)	    Moves t the specified distance in the 
                current direction.
t.pencolor(r, g, b)     Changes the pen color of t to the 
                        specified RGB value or to the specified 
t.pencolor(string)      string, such as "red". Returns the current 
                        color of t when the arguments are omitted.
t.fillcolor(r, g, b)    Changes the fill color of t to the 
t.fillcolor(string)     specified RGB value or to the specified 
                string, such as "red". Returns the current fill 
                color of t when the arguments are omitted.
t.begin_fill()          Enclose a set of turtle commands that will 
t.end_fill()            draw a filled shape using the current fill 
                color.
t.clear()	            Erases all of the turtle’s drawings, 
                without changing the turtle’s state.
t.width(pixels)	        Changes the width of t to the specified 
                number of pixels. Returns t’s current width when 
                the argument is omitted.
t.hideturtle()          Makes the turtle invisible or visible.
t.showturtle()
t.position()	        Returns the current position (x, y) of t.
t.heading()	            Returns the current direction of t.
t.isdown()	            False otherwise.
"""


def draw_square(t, x, y, length):
    """
    Draws a square with turtle, an upper-left corner point
    (x, y), and a side's length.
    """
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


# ====================================================================================================================
"""
syntax for instantiating a class and assigning the resulting 
object to a variable is the following:
<variable name> = <class name>(<any arguments>)
"""
from turtle import Turtle
t = Turtle()

t.width(2)          # for bolder lines
t.left(90)          # turn to face north
t.forward(30)       # draw a vertical line in black
t.left(90)          # turn a face west
t.up()              # prepare to move without drawing
t.forward(10)       # move to beginning of horizontal line
t.setheading(0)     # turn to face east
t.pencolor("red")   # change color to red
t.down()            # prepare to draw
t.forward(20)       # draw a horizontal line in red
t.hideturtle()      # make the turtle invisible


def square(turtl, length):
    """Draws a square with given length."""
    for count in range(4):
        turtl.forward(length)
        t.left(90)

def hexagon(turtl, length):
    """Draws a hexagon with the given length."""
    for count in range(6):
        t.forward(length)
        t.left(60)

def radial_hexagons(turtl, n, length):
    """draws a radial pattern of n hexagons with the given length"""
    for count in range(n):
        hexagon(turtl, length)
        t.left(360 / n)

def radialpattern(t, n, length, shape):
    """draws a radial pattern of n shapes with the given length"""
        for count in range(n):
            shape(t, length)
            t.left(360/n)

    t = Turtle()
    radialPattern(t, n = 10, length = 50, shape = square)
    t.clear()
    radialPattern(t, n = 10, length = 50, shape = hexagon)

# ====================================================================================================================
# Accessor methods
t = Turtle()
t.position()
"""(0.0, 0.0)"""
t.heading()
"""0.0"""
t.isdown()
"""True"""


t.screen.bgcolor("orange")  # changes background color
x = t.screen.window_width()//2  # window width
y = t.screen.window_height()//2  # window height
print((-x, y), (x, -y))

# ====================================================================================================================
# Random Walk
"""
The following script defines a function randomWalk that expects 
as arguments a Turtle object, the number of turns, and distance 
to move after each turn. The distance argument is optional and 
defaults to 20 pixels. When called in this script, the function 
performs 40 random turns with a distance of 30 pixels. 
"""
import random

def randomWalk(t, turns, distance = 20):
    """Turns a random number of degrees and move a given
    distance for a fixed number of turns"""
    for x in range(turns):
        if x % == 0:
            t.left(random.randint(0, 270))
        else:
            t.right(random.randint(0, 270))
        t.forward(distance)
def main():
    t = Turtle()
    t.shape("turtle")
    randomWalk(t, 40, 30)

if __name__ == "__main__":

# ====================================================================================================================
"""
tuple (r, g, b)

Color	Rgb Value
Black	(0, 0, 0)
Red	    (255, 0, 0)
Green	(0, 255, 0)
Blue	(0, 0, 255)
Yellow	(255, 255, 0)
Gray	(127, 127, 127)
White	(255, 255, 255)
"""
 # reference randompatterns.py in book programs
# ====================================================================================================================
# Images Module
"""
Image Method	What It Does
i = Image(filename)	        Loads and returns an image from a 
    file with the given filename. Raises an error if the filename 
    is not found or the file is not a GIF file.
i = Image(width, height)	Creates and returns a blank image 
    with the given dimensions. The color of each pixel is 
    transparent, and the filename is the empty string.
i.getWidth()	            Returns the width of i in pixels.
i.getHeight()	            Returns the height of i in pixels.
i.getPixel(x, y)	        Returns a tuple of integers 
    representing the RGB values of the pixel at position (x, y).
i.setPixel(x, y, (r, g, b))	Replaces the RGB value at the position 
    (x, y) with the RGB value given by the tuple (r, g, b).
i.draw()	                Displays i in a window. The user must 
    close the window to return control to the method’s caller.
i.clone()	                Returns a copy of i.
i.save()	                Saves i under its current filename. 
    If i does not yet have a filename, save does nothing.
i.save(filename)	        Saves i under filename. Automatically 
    adds a .gif extension if filename does not contain it.
"""

from image import Image  # Imports the Image class from the images module
image = Image("smokey.gif")  # Instantiates this class using the file named smokey.gif
image.draw()  # Draws the image

# Once an image has been created, you can examine its width and
# height, as follows:
image.getWidth()
"""198"""
image.getHeight()
"""149"""
#Alternatively, you can print the image’s string representation:
print(image)
"""
Filename: smokey.gif
Width: 198
Height: 149
"""
# getPixel returns a tuple of rgb at given coordinates
image.getPixel(0,0)  #getss rgb at upper left corner
"""(194, 221, 114)"""
# setPixel can replace rgb at given coordinates
image = Image(150, 150)  # Creates a new 150-by-150 image
image.draw()
blue = (0, 0, 225)  # RGB reference
y = image.getHeight() // 2 # Finds middle of page on y-axis
for x in range(image.getWidth()):  # x is entire width of image
    image.setPixel(x, y - 1, blue)   # colors blue horizontal line
    image.setPixel(x, y, blue)  # colors blue horizontal line
    image.setPixel(x, y + 1, blue)  # colors blue horizontal line
image.save("horizontal.gif")
# ====================================================================================================================
# A Loop Pattern for Traversing a Grid
"""prints the pairs of coordinates visited when the outer loop 
traverses the y coordinates:"""
width = 2
height = 3
for y in range(height):
    for x in range(width):
        print((x, y), end = " ")
    print()
"""
(0, 0)(1, 0)
(0, 1)(1, 1)
(0, 2)(1, 2)
"""
# Uses a nested for loop to fill a blank image in red:
image = Image(150, 150)
for y in range(image.getHeight()):
    for x in range(image.getWidth()):
        image.setPixel(x, y, (255, 0, 0))
# ====================================================================================================================
# A Word on Tuples
image = Image("smokey.gif")
(r, g, b) = image.getPixel(0,0) # assigning tuple to 3 variables
# You can now see what the RGB values are
r
"194"
g
"221"
b
"114"
# ====================================================================================================================
# Converting an Image to Black and White
"""The algorithm then resets the pixel’s color values to 0 (black) 
if the average is closer to 0, or to 255 (white) if the average 
is closer to 255."""
def black_and_white(image):
    """Converts the argument image to black adn white"""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)
# testing in script
def main(filename = "smokey.gif"):
    image = Image(filename)
    print("Close the image window to continue.")
    image.draw()
    black_and_white(image)
    print("Close the window to quit.")
    image.draw()
if__name == "__main__":
if __name__ == '__main__':
    main()
# ====================================================================================================================
# Converting an Image to Grayscale
def grayscale(image):
    """Converts the argument image to grayscale."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * .299)
            g = int(r * .587)
            b = int(r * .114)
# ====================================================================================================================
# Copying an image
image = Image("smokey.gif")
image.draw()
newImage = image.clone()  #Creates a copy of the image
newImage.draw()
grayscale(newImage)  #Changes cloned image only
newImage.draw()
image.draw()  #Verify no changes to original
# ====================================================================================================================
# Blurring an image
"""This algorithm resets each pixel’s color to the average of the 
colors of the four pixels that surround it"""
def blur(image):
    """Builds and returns a new image which is a blurred copy of
    the argument image"""

    def triple_sum(triple1, triple2):
        # 1
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return r1 + r2, g1 + g2, b1 + b2
    new = image.clone()
    for y in range(1, image.getHeight() - 1):
        for x in range(1, image.getWidth() - 1):
            oldP = image.getPixel(x, y)
            left =  image.getPixel(x - 1, y)  # to left
            right = image.getPixel(x +1, y)  # to right
            top = image.getPixel(x, y - 1)  # above
            bottom = image.getPixel(x, y + 1)  # below
            sums = reduce(triple_sum, [oldP, left, right, top, bottom])
        # 2
            averages = tuple(map(lambda x: x // 5, sums))
        # 3
            new.setPixel(x, y, averages)
    return new
"""
At #1, the nested auxiliary function tripleSum is defined. This 
function expects two tuples of integers as arguments and returns 
a single tuple containing the sums of the values at each position.

At #2, five tuples of RGB values are wrapped in a list and passed 
with the tripleSum function to the reduce function. This function 
repeatedly applies tripleSum to compute the sums of the tuples, 
until a single tuple containing the sums is returned.

At #3, a lambda function is mapped onto the tuple of sums, and 
the result is converted to a tuple. The lambda function divides 
each sum by 5. Thus, you are left with a tuple of the average RGB 
values.
"""
# ====================================================================================================================
# Edge Detection
def detectEdges (image, amount):
    """Builds and returns a new image in which the edges of the
    argument image are highlighted and the colors are reduced to
    black and white."""

    def average(triple):
        (r. g. b) = triple
        return (r + g + b) // 3

    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    new = image.clone()

for y in range(image.getHeight() - 1):
    for x in range(1, image.getWidth()):
        oldPixel = image.getPixel(x, y)
        leftPixel = image.getPixel(x - 1, y)
        bottomPixel = image.getPixel(x, y + 1)
        oldLum = average(oldPixel)
        leftLum = average(leftPixel)
        bottomLum = average(bottomPixel)
        if abs(oldLum - leftLum) > amount or \
                abs(oldLum - bottomLum) > amount:
            new.setPixel(x, y, blackPixel)
        else:
            new.setPixel(x, y, whitePixel)
return new
# ====================================================================================================================
# Reducing the Image Size
def shrink(image, factor):
    """builds and return a new image which is a smaller copy of
    the argument image, by a the factor argument."""
    width = image.getWidth()
    height = image.getHeight()
    new = Image(width // factor, height // factor)
    oldY = 0
    newY = 0
    while oldY < height -factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    return new

