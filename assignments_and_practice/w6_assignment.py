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
        # Define variables
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

        self._option = input("Choose a menu option from 1-5 or 6 to exit the program: ")

    def run(self):
        """Calls on method that corresponds to menu selection"""
        while True:
            self.menu()

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
            else:
                print("Error: input invalid. Please choose one of the "
                      "prompted options: ")

    def add_order(self):
        """Adds an order to the list"""
        try:
            order_number = int(input("\nEnter your order number: "))
            for _order in self.orders:
                if order_number == _order.get_number():
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
        except ValueError:
            print("Input not recognized, please try again.")

    def delete_order(self):
        """Removes an order from the list"""
        try:
            order_number = int(input("\nEnter your order number: "))
            for burrito_order in self.orders:
                if burrito_order.get_number() == order_number:
                    location = self.orders.index(burrito_order)
                    self.orders.pop(location)
                    print("Removed order")
                    return
            print("Sorry, we could not locate your order.")
        except ValueError:
            print("Input not recognized. Please enter a number")
            self.delete_order()
            return

    def edit_order(self):
        """Changes an order from the list"""
        try:
            order_number = int(input("\nEnter your order number: "))
            for burrito_order in self.orders:
                if burrito_order.get_number() == order_number:
                    order_type = input("Enter your order type: ")
                    order_amount = float(input("Enter your order amount: "))

                burrito_order.set_number(order_number)
                burrito_order.set_type(order_type)
                burrito_order.set_amount(order_amount)
                return
            print("Sorry, we could not locate your order.")
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
        file_name = "Burrito_Orders.txt"
        with open(file_name, 'w') as f:
            for burrito_order in self.orders:
                f.write('Order number: %2s, ' % burrito_order.get_number())
                f.write('Order type: %2s, ' % burrito_order.get_type())
                f.write('Order amount: %2s' % burrito_order.get_amount())
                f.write('\n')


# Run the main class
app = BurritoApp()
app.run()
