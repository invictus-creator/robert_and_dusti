"""
Program: accountBalanceCalculator.py
Author: Robert Timberlake
Compute a user's account balance.
1. The inputs are
    name
    amount 1
    amount 2
    amount 3
    amount 4
    amount 5
3. Computations:
    amount sum = amount 1 + amount 2 + amount 3 + amount 4 + amount 5
4. The outputs are
    amount sum
"""

name = input("Please enter your name: ")
amount1 = float(input("Please enter the first amount: "))
amount2 = float(input("Please enter the second amount: "))
amount3 = float(input("Please enter the third amount: "))
amount4 = float(input("Please enter the fourth amount: "))
amount5 = float(input("Please enter the fifth amount: "))

# Compute the amount sum
amountSum = amount1 + amount2 + amount3 + amount4 + amount5

# Display the account balance
if amountSum > 0:
    print("Your account balance is $%.1f" % amountSum)
elif amountSum == 0:
    print("Your account balance is zero.")
elif amountSum < 0:
    print("Your account is overdrawn. The overdrawn amount is $%.1f" % amountSum)
