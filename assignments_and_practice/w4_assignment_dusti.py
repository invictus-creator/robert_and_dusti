
while True:
    name = input("Enter your name or 'q' to quit: ")

    if name == "q":
        break

    amount = float(input("Enter the amount of your account balance: "))
    transaction = float(input("Enter amount to withdraw (-) or deposit (+): "))

    amount = round(amount + transaction, 2)
    if amount:
        print(f"Your account balance is ${amount:.2f}")
    else:
        print("Your account balance is zero")
