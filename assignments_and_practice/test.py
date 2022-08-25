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
    """Calculates new user balance after withdraw or deposit"""
    try:
        balance = float(input("Please enter your account balance: "))
        amount = float(input("Please amount to withdraw (-) or deposit (+): "))
        return balance + amount
    except ValueError:
        print("Error: Input not recognized. \nPlease enter a positive or negative number.\n")
        return new_balance()


#  Create loop
while True:
    # Get name from user
    name = str(input("Please enter your name or 'q' to quit: "))

    # If user inputs q then end program
    if name == "q":
        break

    current_balance = new_balance()

    # Check if account is overdrawn or zero balance
    if current_balance > 0:
        print("Your account balance is $%.2f" % current_balance)
    elif current_balance == 0:
        print("Your account balance is zero.")
    elif current_balance < 0:
        print("Your account is overdrawn. The overdrawn amount is $%.2f" % current_balance)

print("Exiting Program")
