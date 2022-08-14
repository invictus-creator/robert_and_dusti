"""
This is just code from my week 3 reading.
I'm just using this to reference the main point and lesson.
I wouldn't recommend running this.
"""

# Executing a Statement a Given Number of Times
for eachPass in range(4):
    print("Its alive!", end=" ")

# =====================================================================================================================

number = 2
exponent = 3
product = 1
for eachPass in range(exponent):
    product = product * number
    print(product, end=" ")

# =====================================================================================================================

# Count-Controlled Loops
for count in range(4):
    print(count, end=" ")

# =====================================================================================================================

product = 1
for count in range(1, 5):
    product = product * count

# =====================================================================================================================

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
theSum = 0
for number in range(lower, upper + 1):
    theSum = theSum + number

# =====================================================================================================================

# Traversing the Contents of a Data Sequence
list(range(4))
list(range(1, 5))

# =====================================================================================================================

for number in [6, 4, 8]:
    print(number, end=" ")

for character in ["Hi there!"]:
    print(character, end=" ")

# =====================================================================================================================

# Specifying the Steps in the Range
list(range(1, 6, 1))  # Same as using two arguments
list(range(1, 6, 2))  # Use every other number
list(range(1, 6, 3))  # USe every third number

# =====================================================================================================================

theSum = 0
for count in range(2, 11, 2):
    theSum += count

# =====================================================================================================================

# Loops That Count Down
for count in range(10, 0, -1):
    print(count, end=" ")

list(range(10, 0, -1))

# =====================================================================================================================

# Formatting Text for Output
for exponent in range(7, 11):
    print(exponent, 10 ** exponent)

# =====================================================================================================================
"""
"%6s" % "four"  # right justify
'  four'

"%-6s" % "four"  # left justify
'four  '
"""
# =====================================================================================================================

for exponent in range(7, 11):
    print("%-3d%12d" % exponent, 10 ** exponent)

# =====================================================================================================================

