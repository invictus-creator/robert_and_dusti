"""
Modify the guessing-game program so that the user thinks of a
 number that the computer must guess.
The computer must make no more than the minimum number of
guesses, and it must prevent the user
from cheating by entering misleading hints.
Use I'm out of guesses, and you cheated and
Hooray, I've got it in X tries as your final output.
"""
# Modify the code below:
import random
import math


smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
maxTries = math.ceil(math.log2(larger))
count = 0
while True:
    count += 1
    print(smaller, larger)

    try:
        computerNumber = random.randint(smaller, larger)
    except ValueError:
        count -= 1
        continue

    print("Your number is:", computerNumber)

    correction = input("Enter =, <, or >: ")

    if count > maxTries:
        print("I'm out of guesses, and you cheated!")
        break

    if correction == "<":
        larger = computerNumber - 1
    elif correction == ">":
        smaller = computerNumber + 1
    elif correction == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    else:
        print("Invalid input. Please enter one of the prompted entries")



