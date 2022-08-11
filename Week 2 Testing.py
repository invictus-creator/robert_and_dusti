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
print("The " + m + " chases the " + h)  # what the book wants...(this on the other hand is just fucking stupid to me)


# ASCII Characters & Arithmetic Operators
print(h * 4)  # I'm curious how I would space this
print(10 % 50)  # don't understand what % does
print(25 // 100)  # wtf is a quotient

print(chr(20))  # So I was expecting DC4...idk what is going on
print(ord('R'))  # So the "ord" only accepts a single character. Shouldn't it work for things like DC4 aka 20?
print(chr(65))  # well that worked
print(ord('A'))   # and this works
