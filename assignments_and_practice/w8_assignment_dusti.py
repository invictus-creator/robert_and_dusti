
balance = None
amount = None


def set_balance():
    global balance
    try:
        balance = float(input("Please enter your account balance: "))
    except ValueError:
        print("Error: Input not recognized.")
        balance = None


def set_amount():
    global amount
    try:
        amount = float(input("Please amount to withdraw (-) or deposit (+): "))
    except ValueError:
        print("Error: Input not recognized.")
        amount = None


#  Create loop
while True:
    # Get name from user
    name = str(input("Please enter your name or 'q' to quit: "))

    # If user inputs q then end program
    if name == "q":
        break

    # Get balance and amount in or out from user
    while balance is None:
        set_balance()

    while amount is None:
        set_amount()

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
