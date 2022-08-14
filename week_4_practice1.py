"""
Modify the guessing-game program so that the user thinks of a number that the computer must guess.

The computer must make no more than the minimum number of guesses, and it must prevent the user
from cheating by entering misleading hints.
Use I'm out of guesses, and you cheated and Hooray, I've got it in X tries as your final output.

Enter the smaller number: 0
Enter the larger number: 50
0 50
Your number is 25
Enter =, <, or >: <
0 24
Your number is 12
Enter =, <, or >: <
0 11
Your number is 5
Enter =, <, or >: <
0 4
Your number is 2
Enter =, <, or >: <
0 1
Your number is 0
Enter =, <, or >: >
1 1
Your number is 1
Enter =, <, or >: >
I'm out of guesses, and you cheated!

"""
# Modify the code below:
import random

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
    count += 1
    geussed = print(myNumber)
    userNumber = (input("Enter =, <, or >: "))
    if userNumber == "<":
        myNumber = random.radiant(smaller, geussed)
    elif userNumber == ">":
        myNumber = random.radiant(geussed, larger)
    else:
        print("Hooray, I've got it in", count, "tries!")
        break
