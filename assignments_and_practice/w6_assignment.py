"""
Program: w6_assignment.py
Author: Robert Timberlake
Creates a list of burrito orders using classes and methods
1. The inputs are
    menu selection
    order number
    order type
    order amount
2. The outputs are
    order list
"""
import pickle


class BurritoOrder(object):

    def __init__(self):
        self._number = None
        self._type = None
        self._amount = None

    def set_amount(self, order_amount):
        self._amount = order_amount

    def get_amount(self):
        return self._amount

    def set_type(self, order_type):
        self._type = order_type

    def get_type(self):
        return self._type

    def set_number(self, order_number):
        self._number = order_number

    def get_number(self):
        return self._number


class BurritoApp(object):
    _option = None
    orders = []  # Creates order list

    def menu(self):
        """Displays the menu and inputs """
        print("\n********** Main Menu ***********")
        print("1. Add Order")
        print("2. Delete Order")
        print("3. Edit Order")
        print("4. Display Order")
        print("5. Save Order")
        print("6. Exit the Program")
        # Request user input for menu selection
        self._option = input("Choose a menu option from 1-5 or 6 to exit the program: ")

    def run(self):
        """Main program loop. Calls on menu and starts user selected choice."""
        while True:
            self.menu()  # calls menu and gets returned choice

            # Call on method that corresponds to user choice
            if self._option == "1":
                self.add_order()
            elif self._option == "2":
                self.delete_order()
            elif self._option == "3":
                self.edit_order()
            elif self._option == "4":
                self.display_orders()
            elif self._option == "5":
                self.save_orders()
            elif self._option == "6":
                print("Exiting program")
                break
            else:  # If user choice does not correspond to a method display an error and restart loop
                print("Error: input invalid. Please choose one of the "
                      "prompted options: ")

    def add_order(self):
        """Adds an order to the list"""
        try:
            order_number = int(input("\nEnter your order number: "))

            # Check if existing order already exists with order number
            for _order in self.orders:
                if order_number == _order.get_number():
                    # Display error and restart method if order number collision found
                    print("Order number already exists. Please Enter a different number.")
                    self.add_order()
                    return

            order_type = input("Enter your order type: ")
            order_amount = float(input("Enter your order amount: "))

            burrito_order = BurritoOrder()
            burrito_order.set_number(order_number)
            burrito_order.set_type(order_type)
            burrito_order.set_amount(order_amount)

            self.orders.append(burrito_order)
        # Handle value errors
        except ValueError:
            while True:
                choice = input("Input not recognized. Input 'q' to quit to main menu or press 'enter' to try again:")
                if choice == "q":
   1
self.run()
                elif choice == "":
                    self.add_order()
                else:
                    continue

    def delete_order(self):
        """Removes an order from the list"""
        try:
            order_number = int(input("\nEnter your order number: "))
            for burrito_order in self.orders:
                if burrito_order.get_number() == order_number:  # Checks if order number exists
                    location = self.orders.index(burrito_order)  # Gets the order location
                    self.orders.pop(location)  # Removes order
                    print("Removed order")
                    return
            while True:
                    choice = input("Sorry, we could not locate your order. Input 'q' to quit to the main menu or "
                                   "press enter to try again:")
                    if choice == "q":
                        self.run()
                    elif choice == "":
                        self.delete_order()
                    else:
                        continue
            print()
        # Handle value errors
        except ValueError:
            print("Input not recognized. Please enter a number")
            self.delete_order()
            return

    def edit_order(self):
        """Changes an order from the list"""
        try:
            order_number = int(input("\nEnter your order number: "))
            for burrito_order in self.orders:
                if burrito_order.get_number() == order_number:  # Checks if order number exists
                    order_type = input("Enter your order type: ")  # Changes order type
                    order_amount = float(input("Enter your order amount: "))  # Changes order amount

                    # Save edited order
                    burrito_order.set_number(order_number)
                    burrito_order.set_type(order_type)
                    burrito_order.set_amount(order_amount)
                    return
            else:
                while True:
                    choice = input("Sorry, we could not locate your order. Input 'q' to quit to the main menu or "
                                   "press enter to try again:")
                    if choice == "q":
                        self.run()
                    elif choice == "":  # enter should restart method
                        self.edit_order()
                    else:
                        continue

        # Handle value errors
        except ValueError:
            print("Input not recognized, please enter a number.")
            self.edit_order()
            return

    def display_orders(self):
        """Displays order list"""
        print("\n******** Current Orders ********")

        for burrito_order in self.orders:
            print("Order number: %2s" % burrito_order.get_number())
            print("Order type: %2s" % burrito_order.get_type())
            print("Order amount: %2s" % burrito_order.get_amount())

    def save_orders(self):
        """Saves the order list to a file"""
        file_name = "Burrito_Orders.txt"  # Assigns variable to file name
        with open(file_name, 'w') as f:  # Opens file
            for burrito_order in self.orders:  # Saves all orders from list into file
                f.write('Order number: %2s, ' % burrito_order.get_number())
                f.write('Order type: %2s, ' % burrito_order.get_type())
                f.write('Order amount: %2s' % burrito_order.get_amount())
                f.write('\n')
        print("All orders saved successfully.")


# Run the main class
app = BurritoApp()
app.run()
