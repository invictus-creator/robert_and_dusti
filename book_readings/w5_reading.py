#  List Literals and Basic Operators
[1950, 1952, 1958]  # A list of integers
["apples", "oranges", "cherries"]  # A list of strings
[[1920, 1921], [1922, 1923]]  # List of of lists

import math

x = 2
[x, math.sqrt(x)]
"""[2, 1.1421356237309]"""
[x + 1]
"""[3]"""
# ====================================================================================================================
# List assignment to variables
first = [1, 2, 3, 4]
second = list(range(1, 5))
first
"""[1, 2, 3, 4]"""
second
""""[1, 2, 3, 4]"""
# ====================================================================================================================
# List use on a string
third = list("Hi there!")
third
"""['H', 'i', ' ', 't', 'h', 'e', 'r', 'e', '!']"""
# ====================================================================================================================
# len with a string
len(first)  # len shows the number of items in an object
"""4"""
first[0]  # I'm confused. I believe this references the first element in list "first" TODO
"""1"""
first[2:4]  # I'm confused. Book says this slices for a sublist TODO
"""[3, 4]"""
# ====================================================================================================================
# Concatenation with a list
first = [5, 6]
"""[1, 2, 3, 4, 5, 6]"""
first == second
"""True"""
# ====================================================================================================================
# print formatting behavior with lists
print("1234")
"""1234"""
print([1, 2, 3, 4])
"""[1, 2, 3, 4]"""

for w in [1, 2, 3, 4]:  # prints list without brackets
    print(w, end=" ")
"""1 2 3 4"""
# ====================================================================================================================
# use in to see if something is inside list
3 in [1, 2, 3]
"""True"""
0 in [1, 2, 3]
"""False"""
# ====================================================================================================================
"""
   Operator or Function	                What It Does
L[<an integer expression>]	        Subscript used to access an element at the given index position.
L[<start>:<end>]	                Slices for a sublist. Returns a new list.
L1 + L2	                            List concatenation. Returns a new list consisting of the elements of the two operands.
print(L)	                        Prints the literal representation of the list.
len(L)	                            Returns the number of elements in the list.
list(range(<upper>))	            Returns a list containing the integers in the range 0 through upper - 1.
==, !=, <, >, <=, >=	            Compares the elements at the corresponding positions in the operand lists. Returns True if all the results are true, or False otherwise.
for <variable> in L: <statement>	Iterates through the list, binding the variable to each element.
<any value> in L	                Returns True if the value is in the list or False otherwise.

"""
# ====================================================================================================================
# Replacing an Element in a List
example = [1, 2, 3, 4]
example
"""[1, 2, 3, 4]"""
example[3] = 0  # changes third value to 0
example
"""[1, 2, 3, 0]"""

numbers = [2, 3, 4, 5]
numbers
"""[2, 3, 4, 5]"""
for index in range(len(numbers)):  # I believe this is saying do this for the entire list
    numbers[index] = numbers[index] ** 2  # I believe this is referencing each position TODO
numbers
"""[4, 9, 16, 25]"""
# ====================================================================================================================
# Splitting a string
sentence = "This example has five words."
words = sentence.split()  # essentially turning each word into a element in a list
words
"""['This', 'example', 'has', 'five', 'words.']"""
for index in range(len(words)):
    words[index] = words[index].upper()  # capitalizes each position
words
"""['THIS', 'EXAMPLE', 'HAS', 'FIVE', 'WORDS.']"""
# ====================================================================================================================
"""
  List Method	                        What It Does
L.append(element)	        Adds element to the end of L.
L.extend(aList)	            Adds the elements of aList to the end of L.
L.insert(index, element)	Inserts element at index if index is less than the length of L. Otherwise, inserts element at the end of L.
L.pop()	                    Removes and returns the element at the end of L.
L.pop(index)	            Removes and returns the element at index.
"""
# ====================================================================================================================
# List Methods for Inserting and Removing Elements
example = [1, 2]
example
"""[1, 2]"""
example.insert(1, 10)
example
"""[1, 10, 2]"""
example.insert(3, 25)
example
"""[1, 10, 2, 25]"""
# ====================================================================================================================
# Using append and extend
example = [1, 2]
example
"""[1, 2]"""
example.append(3)  # adds value "3" to end of list
example
"""[1, 2, 3]"""
example.extend([11, 12, 13])  # adds list inside () to end of "example" list
example
"""[1, 2, 3, 11, 12, 13]"""  # note how here "example" is now changed to the new list
example + [14, 15]
"""[1, 2, 3, 11, 12, 13, 14, 15]"""
example
"""[1, 2, 3, 11, 12, 13]"""  # note how adding list did not change original list
# ====================================================================================================================
# Using pop
example
"""[1, 2, 3, 11, 12, 13]"""
example.pop()  # if left unspecified it removes last value
example
"""[1, 2, 3, 11, 12]"""
example.pop(1)  # removes second value
"""2"""
example
"""[1, 10, 11, 12]"""
# ====================================================================================================================
# Using index to find where a value is in a list
aList = [34, 45, 67]
target = 45
if target in aList:  # searches for target first (without this you could get an error using index)
    print(aList.index(target))  # prints the position of target in list
else:
    print(-1)  # could not find target
# ====================================================================================================================
# Sorting a List
example = [4, 2, 10, 8]
example
"""[4, 2, 10, 8]"""
example.sort()
example
"""[2, 4, 8, 10]"""
# ====================================================================================================================
# Mutator Methods and the Value None
first = [10, 20, 30]
second = first
first[1] = 99
first
"""[10, 99, 30]"""
second
"""[10, 99, 30]"""  # notice how "second" also gets changed

third = []
for element in first:
    third.append(element)  # adds "first" list to end of "third"
first
"""[10, 99, 30]"""
third
"""[10, 99, 30]"""
first[1] = 100
first
"""[10, 100, 30]"""
third
"""[10, 99, 30]"""
# this could also be achieved with list function
third = list(first)
# ====================================================================================================================
# Using a List to Find the Median of a Set of Numbers
"""
File: median.py
Prints the median of a set of numbers in a file.
"""

fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# Input the text, convert it to numbers, and
# add the numbers to a list
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))

# Sort the list and print the number at its midpoint
numbers.sort()
midpoint = len(numbers) // 2
print("The median is", end=" ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
"""
When run with a file thats contents are: 
3 2 7
8 2 1
5
the output is:
The median is 3.0
"""
# ====================================================================================================================
""" A tuple is the same thing as a list except instead of "[]"
you would use () which makes is immutable"""


# ====================================================================================================================
# Simple functions
def average(lyst):
    """Returns the average of the numbers in lyst."""
    theSum = 0
    for number in lyst:
        theSum += number
    return theSum / len(lyst)


average([1, 3, 5, 7])  # calling on our function "average"
"""4.0"""


# ====================================================================================================================
def odd(x):
    """Returns True if x is odd or False otherwise"""
    if x % 2 == 1:  # can we go over % again TODO
        return True
    else:
        return False


odd(5)
"""True"""
odd(6)
"""False"""
# ====================================================================================================================
"""
File: computesquare.py
Illustrates the definition of a main function.
"""


def main():
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)


def square(x):
    """Returns the square of x. """
    return x * x


# The entry point for program execution
if __name__ == "__main__":
    main()
# ====================================================================================================================
info = {}
info["name"] = "Sandy"
info["occupation"] = "hacker"
info
"""{'name': 'Sandy', 'occupation': hacker'}"""

info["occupation"] = "manager"
info
"""{'name': 'Sandy', 'occupation': 'manager'}"""

print(info.get("job", None))  # Look for job in "info" and returns none if there is no entry
"""None"""
# ====================================================================================================================
# Removing dictionary entry
print(info.pop("job", None))
"""None"""
print(info.pop("occupation"))
"""manager"""
info
"""{'name':'Sandy'}"""
# ====================================================================================================================
# Traversing a Dictionary
for key in info:
    print(key, info[key])
# ====================================================================================================================
grades = {90: 'A', 80: 'B', 70: 'C'}
list(grades.items())
"""[(80, 'B'), (90, 'A'), (70, 'C')]"""
# ====================================================================================================================
for (key, value) in grades.items():
    print(key, value)
# ====================================================================================================================
theKeys = list(info.keys())
theKeys.sort()
for key in theKeys:
    print(key, info[key])
# ====================================================================================================================
"""
Dictionary Operation	         What It Does
len(d)	                Returns the number of entries in d.
d[key]	                Used for inserting a new key, replacing a value, or obtaining a value at an existing key.
d.get(key [, default])	Returns the value if the key exists or returns the default if the key does not exist. Raises an error if the default is omitted and the key does not exist.
d.pop(key [, default])	Removes the key and returns the value if the key exists or returns the default if the key does not exist. Raises an error if the default is omitted and the key does not exist.
list(d.keys())	        Returns a list of the keys.
list(d.values())	    Returns a list of the values.
list(d.items())	        Returns a list of tuples containing the keys and values for each entry.
d.clear()	            Removes all the keys.
for key in d:	        key is bound to each key in d in an unspecified order.
"""
# ====================================================================================================================
# Hexadecimal System
hexToBinaryTable = {'0': '0000', '1': '0001', '2': '0010',
                    '3': '0011', '4': '0100', '5': '0101',
                    '6': '0110', '7': '0111', '8': '1000',
                    '9': '1001', 'A': '1010', 'B': '1011',
                    'C': '1100', 'D': '1101', 'E': '1110',
                    'F': '1111'}


def convert(number, table):
    """Builds and returns the base two representation of
   number. """
    binary = ""
    for digit in number:
        binary = table[digit] + binary
    return binary


print(convert("35A", hexToBinaryTable))
# ====================================================================================================================
# Finding the Mode of a List of Values
"""
File: mode.py
Prints the mode of a set of numbers in a file.
"""

fileName = input("Enter the file name: ")
f = open(fileName, 'r')

# Input the text, convert its to words to uppercase, and
# add the words to a list
words = []
for line in f:
    wordsInLine = line.split()
    for word in wordsInLine:
        words.append(word.upper())

# Obtain the set of unique words and their
# frequencies, saving these associations in
# a dictionary
theDictionary = {}
for word in words:
    number = theDictionary.get(word, None)
    if number == None:
        # word entered for the first time
        theDictionary[word] = 1
    else:
        # word already seen, increment its number
        theDictionary[word] = number + 1

# Find the mode by obtaining the maximum value
# in the dictionary and determining its key
theMaximum = max(theDictionary.values())
for key in theDictionary:
    if theDictionary[key] == theMaximum:
        print("The mode is", key)
        break
