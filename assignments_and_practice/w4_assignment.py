"""
Program: w4_assignment.py
Author: Robert Timberlake
Compute a user's account balance.
1. The inputs are
    name
    balance
    amount in or out
3. Computations:
    updated balance = balance + amount in or out
4. The outputs are
    updated balance
"""
#  Create loop
while True:
    # Get name from user
    name = input("Please enter your name or 'q' to quit: ")

    # If user inputs q then end program
    if name == "q":
        break

    # Get balance and amount in or out from user
    balance = float(input("Please enter your account balance: "))
    amount = float(input("Please amount to withdraw (-) or deposit (+): "))

    #  Calculate new balance
    newBalance = balance + amount

    # Check if account is overdrawn or zero balance
    if newBalance > 0:
        print("Your account balance is $%.2f" % newBalance)
    elif newBalance == 0:
        print("Your account balance is zero.")
    elif newBalance < 0:
        print("Your account is overdrawn. The overdrawn amount is $%.2f" % newBalance)

print("Exiting Program")
