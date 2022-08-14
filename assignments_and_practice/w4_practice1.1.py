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



