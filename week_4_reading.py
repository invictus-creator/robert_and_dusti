"""
This is just code from my week 4 reading.
I'm just using this to reference the main point and lesson.
I wouldn't recommend running this.
"""

#  The Structure and Behavior of a while Loop

theSum = 0.0
data = input("Please enter a number or press enter to quit: ")
while data != "":
    number = float(data)
    theSum += number
    print(input("Please enter another number or press enter to quit: "))
print("The sum is: ", theSum)

# =====================================================================================================================

#  Summation with a for loop
theSum = 0
for count in range(1, 11):
    theSum += count
print(theSum)

# =====================================================================================================================

#  Summation with a while loop
theSum = 0
count = 1
while count <= 10:
    theSum += count
    count += 1
print(theSum)

# =====================================================================================================================

#  Counting down with a for loop
for count in range(10, 1, -1):
    print(count, end=" ")

# =====================================================================================================================

#  Counting down with a while loop
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1

# =====================================================================================================================

#  The while True Loop and the break Statement
theSum = 0.0
while True:
    data = input("Please enter or number or press enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
print(theSum)

# =====================================================================================================================

while True:
    grade = int(input("Please enter your numerical grade: "))
    if 0 <= grade <= 100:
        break
    else:
        print("Error: You must enter grade between 0 and 100")
if grade < 60:
    print("You failed!")
else:
    print("You passed!")

# =====================================================================================================================

while True:
    grade = int(input("Please enter your numerical grade: "))
    if grade < 0 or grade > 100:
        print("Error: You must enter grade between 0 and 100")
    else:
        if grade < 60:
            print("You failed!")

        else:
            print("You passed!")
        break

# =====================================================================================================================

done = False
while not done:  # Why does the "not" have to be here nad why does it behave like it does without it
    grade = int(input("Please enter your numerical grade: "))
    if 0 <= grade <= 100:
        done = True
    else:
        print("Error: You must enter a grade between 0 and 100")
print(grade, "is your grade.")

# =====================================================================================================================

#  Random Numbers

import random   # So I cant put this here? Stupid

for roll in range(4):
    print(random.randit(1, 6), end=" ")

# =====================================================================================================================
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))
randNumber = random.randint(low, high)
count = 0
while True:
    count += 1
    guessedNumber = int(input("Enter you guessed number: "))

    if guessedNumber < randNumber:
        print("Your too low")
    elif guessedNumber > randNumber:
        print("Your too high")
    else:
        print("Congrats! You guessed the number in", count, "tries!")
        break
