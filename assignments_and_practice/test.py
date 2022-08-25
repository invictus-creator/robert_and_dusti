"""
Program: w8_assignment.py
Author: Robert Timberlake
Modify the program from week 4 to handle any errors and exceptions that you can find.
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

def new_balance():
    """Calculates new balance of user after withdraw or deposit"""
    try:
        balance = float(input("Please enter your account balance: "))
        amount = float(input("Please amount to withdraw (-) or deposit (+): "))
        current_balance = balance + amount
        return current_balance
    except ValueError:
        print("Error: Input not recognized. \nPlease enter a positive or negative number.\n")
        new_balance()

#  Create loop
while True:
    # Get name from user
    name = str(input("Please enter your name or 'q' to quit: "))

    # If user inputs q then end program
    if name == "q":
        break
    new_balance()

    # Check if account is overdrawn or zero balance
    elif newBalance > 0:
        print("Your account balance is $%.2f" % newBalance)
    elif newBalance == 0:
        print("Your account balance is zero.")
    elif newBalance < 0:
        print("Your account is overdrawn. The overdrawn amount is $%.2f" % newBalance)

print("Exiting Program")

