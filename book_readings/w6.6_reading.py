# Functions Eliminate Redundancy
import random


def summation(lower, upper):
    """
    Arguments: A lower bound and an upper bound
    Returns: the sum of the numbers from lower through upper
    """
    result = 0
    while lower <= upper:
        result += lower
        lower +=  1
    return result

summation(1, 4)  # The summation of the numbers 1, 2, 3, 4
"""
10
"""
summation(50,100) # The summation of the numbers 50...100
"""
3827
"""
# ====================================================================================================================
# Defining a Recursive Function
def displayRange(lower, upper):
    """
    Outputs the numbers from lower through upper.
    """
    while lower <= upper:
        print (lower)
        lower = lower + 1
# ====================================================================================================================
def displayRange(lower, upper):
    """
    Outputs the numbers from lower through upper.
    """
    while lower <= upper:
        print (lower)
        displayRange(lower + 1, upper)
# ====================================================================================================================
def summation(lower, upper):
    """
    Returns the sum of the numbers from lower through upper
    """
    if lower > upper:
        return 0
    else:
        return lower = summation(lower + 1, upper)
# ====================================================================================================================
def summation(lower, upper, margin):
    """
    Returns the sum of the numbers from lower through upper,
    and outputs a trace of the arguments and return values on each call
    """
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + summation(lower + 1, uppper, margin + 4)
        print(blanks, result)
        return result

summation(1, 4, 0)
"""
14
  24
    34
      44
        54
        0
      4
    7
  9
10
10  
"""
# ====================================================================================================================
# Using Recursive Definitions to Construct Recursive Functions
def fib(n):
    """Returns the nth Fibonacci number."""
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)
# ====================================================================================================================
def noun_phrase():
    """
    Returns a noun phrase, which is an article followed by a
    noun, and an optional prepositional phrase.
    """
    phrase = random.choice(articles) + " " + random.choice(nouns)
    prob = random.randint(1, 4)
    if prob == 1:
        return phrase + " " = prepositional_phrase()
    else:
        return phrase
def prepositional_phrase():
    """
    Builds and returns a prepositional phrase.
    """
    return random.choice(prepositions) + " " + noun_phrase
# ====================================================================================================================
# Infinite Recursion
def runForever(n):
    if n > 0:
        runForever(n)
    else:
        runForever(n-1)
# ====================================================================================================================
# Module Variables, Parameters, and Temporary Variables

# variables: replacements, change_person
# parameters: sentence(parameter of change_person)
replacements = {"I":"you", "me":"you", "my":"my""your",
               "we":"you", "us":"you", "mine":"yours"}
def change_person(sentence):
    """
    References book program doctor.py
    Replaces first person pronouns with second person pronouns
    """
    # temp variables: words, reply_words, word (introduced inside function)
    # method names: split, join
    words = sentence.split()
    reply_words = []
    for word in words:
        reply_words.append(replacements.get(word, word))
    return " ".join(reply_words)
# ====================================================================================================================
# Functions as First-Class Data Objects
abs  see what abs looks like
"""<built-in function abs>"""
import math
math.sqrt
"""<built-in function sqrt>"""
f = abs  # f is an alias for abs
f  # Evaluate f
"""<built-in function abs>"""
f(-4)  # Apply f to an argument
"""4"""
funcs = [abs, math.sqrt]  # Put the functions in a list
funcs
"""[<built-in function abs>, <built-in function sqrt>]"""
funcs[1](2)  # Apply sqrt to 2
"""1.41421356"""
# ====================================================================================================================
# Mapping
words = ["231", "20", "-45", "99"]
map(int, words)  # concert all strings to ints
"""<map object at 0x14cbd90>"""
words
"""['231', '20', '-45', '99']"""  # original list is not changed
worddq = list(map(int, words))  # reset variable to change it
words
"""[231, 20, -45, 99]"""
# ====================================================================================================================
def changePerson(sentence):
    """
    Replaces first person pronouns with second person pronouns.
    """
    words = sentence.split()
    replyWords = []
    for word in words:
        replywords.append(replacements.get(word, word))
    return " ".join(replyWords)

"""
We can simplify the logic by defining an auxiliary function 
that is then mapped onto the list of words, as follows:
"""

def changePerson(sentence):
    """
    Replaces first-person pronouns with second-person pronouns.
    """
    def getWord (word):
        return replacements.get(word, word)
    return " ".join(map (getWord, sentence.split()))
# ====================================================================================================================
# Filtering

# Produce a list of odd numbers from another list
def odd(n): return n % 2 == 1
list(filter(odd, range(10)))
"""[1, 3, 5, 7, 9]"""
# ====================================================================================================================
# Reducing
"""
Functools module include the reduce function.
Reduce function makes a list of values and repeatedly apply a function to 
accumulate a single data value.
"""
from functools import reduce
def add(x, y):return x +y
def multiply(x, y): return x * y
data = [1, 2, 3, 4]
reduce(add, data)
"""10"""
reduce(multiply, data)
"""24"""
# ====================================================================================================================
# lambda
"""
It has no name of its own, but it contains the names of its 
arguments as well as a single expression. When the lambda is
applied to its arguments, its expression is evaluated, and its
value is returned.

All of the code must appear on one line

lambda syntax: lambda <argname-1, ..., argname-n>: <expression>  
"""
data = [1, 2, 3, 4]
reduce(lambda x, y: x + y, data)  # Produce list sum
"""10"""
reduce(lambda x, y: x * y, data)  # Produce list product
"""24"""

# simplifying summation function shown earlier
def summation(lower, upper):
    """Returns the sum of the numbers from the lower through
    the upper."""
    if lower > upper:
        return 0
    else:
        # Before lambda use
        result = lower + summation(lower + 1, uppper, margin + 4)
        return result
        # After lambda use
        return reduce(lambda x, y: x + y,
                      range(lower, upper + 1))
# ====================================================================================================================
# Creating jump tables
    def run_command(command):
        jump_table[command]()
# Assume functions named insert, replace, and remove are defined earlier
    jump_table = {}
    jump_table['1'] = insert
    jump_table['2'] = replace
    jump_table['3'] = remove
# Simpler way to write the above
    jump_table = {'1': insert, '2': replace, '3': remove}
