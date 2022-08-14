
while True:
    name = input("Please enter your name or 'q' to quit: ")
    if name == "q":
        break
    balance = float(input("Please enter your account balance: "))
    amount = float(input("Please amount to withdraw (-) or deposit (+): "))
    newBalance = balance + amount
    if newBalance > 0:
        print("Your account balance is $%.2f" % newBalance)
    elif newBalance == 0:
        print("Your account balance is zero.")
    elif newBalance < 0:
        print("Your account is overdrawn. The overdrawn amount is $%.2f" % newBalance)
print("Exiting Program")
