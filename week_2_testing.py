"""I'm just playing around with some things from Week 2's reading.
Still no rocket science :( """
# testing glue or concatenating of expressions
x = "mike "
y = "tom"
z = x + y  # this is how I would do it
print(z)

a = "mark"
b = "twain"
c = a + " " + b  # this is how the book says to do it (I understand going this route instead)
print(c)

h = "hooker"
m = "meth head"
print("The", m, "chases the", h)  # what I would do

# ======================================================================================================================
print(f"The {m} chases the {h}")  # how i would do it
# ======================================================================================================================


print("The " + m + " chases the " + h)  # what the book wants...(this on the other hand is just fucking stupid to me)

# ASCII Characters & Arithmetic Operators

# ======================================================================================================================
print("\nAdding spaces")
print("-" * 40)

print(h * 4)  # I'm curious how I would space this

"""
There are a couple ways to do this. 
"""

# add a space at the end, then multiply the result by 4
print((h + " ") * 4)

# change the variable to include a space
h = h + " "
print(h * 4)

# this is excessive, but demonstrates another way to build strings, use the join method on list objects
h = "hooker"
hookers = []
for _ in range(4):
    hookers.append(h)

print(f"list of hookers: {hookers}")
print(f"join with ' ' -> {' '.join(hookers)}")
print(f"join with ',' -> {','.join(hookers)}")
print(f"join with ' chokes ' -> {' chokes '.join(hookers)}")

# ======================================================================================================================
print("\nModular Arithmetic")
print("-" * 40)

print(10 % 50)  # don't understand what % does

""" 
This is called modular arithmetic, the % is the modulo operator. It's a confusing thing to get your head around. It's 
math done on a circular line. The best way to understand it is to think of a clock. There are 12 numbers on a clock and
you want to know what number the hand will point to at 17:00 military time.
"""

print(f"17 mod 12 = {17 % 12}")

# =======================================================================================================================
print("\nQuotient")
print("-" * 40)

print(25 // 100)  # wtf is a quotient

"""
The quotient is the whole number from a division.
"""

print(f"10 / 3 = {10 / 3}")
print(f"quotient of 10 / 3 = {10 // 3}")

# =======================================================================================================================
print("\nExponents")
print("-" * 40)

print(2 ** 3 ** 2)  # youll have to explain this one to me

"""
In python, ** is how you do exponents in python. 3 to the power of 3 (3^3) is 3**3 
"""

print(f"3^3 = {3 ** 3}")

# =======================================================================================================================
print("\nASCII Characters")
print("-" * 40)

print(chr(20))  # So I was expecting DC4...idk what is going on
print(ord('R'))  # So the "ord" only accepts a single character. Shouldn't it work for things like DC4 aka 20?
print(chr(65))  # well that worked
print(ord('A'))  # and this works

"""
So this is the interesting part, it looks like anything 31 or less I would call a special character that does something
when read by the computer. DC4 doesn't display as 'DC4' it stands for 'device control 4'. Which doesn't really do 
anything. But to better understand this, integar 13 is 'carriage return' and will place the cursor at the beginning of
the line. And 8 is 'backspace'.
"""

print("\ncarriage return")
print("abc" + chr(13) + "123")  # notice how the cursor went back to the start and typed over 'abc'
print("abcdef" + chr(13) + "123")  # the whole line is rewritten, so 'def' is gone too

print("\nbackspace")
print("abc" + chr(8) + "123")  # backspace once
