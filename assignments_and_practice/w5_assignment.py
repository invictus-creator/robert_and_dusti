"""
Program: w5_assignment.py
Author: Robert Timberlake
Allows a user to add, remove, and edit transactions in a list
"""


# Create a function that displays a menu and returns the choice
def menu():
    """
    Displays an option menu for user to select 1 of 5 options:
    1. Add Transaction
    2. Delete Transaction
    3. Edit Transaction
    4. Display Transaction
    5. Exit the Program

    Returns: option
    """
    print("\n********** Main Menu ***********")
    print("1. Add Transaction")
    print("2. Delete Transaction")
    print("3. Edit Transaction")
    print("4. Display Transactions")
    print("5. Exit the Program")

    _option = input("Choose a menu option from 1-4 or 5 to exit the program: ")
    return _option


# Create a function that adds a value to the list
def add_trans(transaction):
    """
    Adds user input to parameter list
    """
    key = input("Enter the transaction key to add: ")
    transaction.append(key)
    print("Added")


# Create a function that deletes specified value from list
def delete_trans(transaction):
    """
    Removes user input from parameter list
    """
    key = input("Enter the transaction key to delete: ")

    # Checks if key in parameters first to prevent value error
    try:
        transaction.remove(key)
    except ValueError:
        print("'%.2s' was not found in the transactions." % key)
        return
    print("Successfully deleted the transaction.")


# Create a function that replaces specified value in list
def edit_trans(transaction):
    """
    Asks user for key to replace and what to put in its place.
    Replaces old key with new key in parameter list
    """
    old_key = input("Enter the transaction key to edit: ")

    # Checks if key in parameters first to prevent value error
    try:
        location = transaction.index(old_key)
    except ValueError:
        print("'%s' was not found in the transactions." % old_key)
        return

    new_key = input("Enter the new transaction key to add: ")

    transaction.remove(old_key)
    transaction.insert(location, new_key)


# Create a function that displays keys in the list
def display_trans(transaction):
    """
    Prints the transactions list
    """
    print("** Transactions **")
    for index, item in enumerate(transaction):
        print(f"{index + 1}. {item}")


# Define list variable
transactions = []

# Start main loop
while True:
    # Call on menu function
    option = menu()

    # Handle user input that is returned from menu function
    if option == "1":
        add_trans(transactions)
    elif option == "2":
        delete_trans(transactions)
    elif option == "3":
        edit_trans(transactions)
    elif option == "4":
        display_trans(transactions)
    elif option == "5":
        print("Exiting the program")
        break
    else:
        print("Error: input invalid. Please choose one of the prompted options: ")
