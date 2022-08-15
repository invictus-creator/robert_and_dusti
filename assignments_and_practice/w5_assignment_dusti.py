def display_menu():
    """
    Displays a menu so that the user can select 1 of 5 options:
        1. Add Transaction
        2. Delete Transaction
        3. Edit Transaction
        4. Display Transaction
        5. Exit the Program

    Returns: int

    """
    print("\n********** Main Menu ***********")
    print()
    print("1. Add Transaction")
    print("2. Delete Transaction")
    print("3. Edit Transaction")
    print("4. Display Transactions")
    print("5. Exit the Program")

    try:
        option = int(input("Selection> "))
    except ValueError:
        option = 0

    return option


def add_transaction(transactions: list):
    """
    Asks user to enter transaction key and appends key to transactions list

    Args:
        transactions: list

    Returns:

    """
    key = input("Enter new transaction key: ")
    transactions.append(key)
    print("Added")


def delete_transaction(transactions: list):
    """
    Asks user to enter transaction key and deletes key from transactions list

    Args:
        transactions: list

    Returns:

    """
    key = input("Enter transaction key to delete: ")

    try:
        transactions.remove(key)
    except ValueError:
        print(f"'{key}' not in list")
        return

    print("Removed")


def edit_transaction(transactions: list):
    """
    Asks user to enter transaction key to edit, then asks for new value and changes key in transactions list

    Args:
        transactions: list

    Returns:

    """
    old_key = input("Enter the transaction key to edit: ")

    try:
        _index = transactions.index(old_key)
    except ValueError:
        print(f"'{old_key}' not in list")
        return

    new_key = input("Enter the new transaction key: ")

    transactions.remove(old_key)
    transactions.insert(_index, new_key)

    print("Changed")


def display_transactions(transactions: list):
    """
    Prints the transactions list

    Args:
        transactions: list

    Returns:

    """
    print()
    print("*" * 16)
    print("* Transactions *")
    print("*" * 16)

    for index, transaction in enumerate(transactions):
        print(f"{index + 1}. {transaction}")

    print("*" * 16)


# Main loop
transactions = []
while True:
    option = display_menu()

    if option == 1:
        add_transaction(transactions)
    elif option == 2:
        delete_transaction(transactions)
    elif option == 3:
        edit_transaction(transactions)
    elif option == 4:
        display_transactions(transactions)
    elif option == 5:
        print("Exiting program")
        break
    else:
        print("Option not available. Please choose 1 to 5.")
