from os.path import dirname

PATH = dirname(__file__)


class PizzaOrder(object):
    """Pizza Order
    """

    def __init__(self):
        self._amount = None
        self._type = None
        self._number = None

    def __str__(self):
        return f"Order number: {self._number}\n" \
               f"Order type: {self._type}\n" \
               f"Order amount: {self._amount}"

    def set_amount(self, order_amount):
        self._amount = order_amount

    def set_type(self, order_type):
        self._type = order_type

    def set_number(self, order_number):
        self._number = order_number

    def get_amount(self):
        return self._amount

    def get_type(self):
        return self._type

    def get_number(self):
        return self._number


class PizzaApp(object):
    """Application for pizza orders
    """
    choice = None
    orders = []

    def get_order_from_list(self, order_number):
        """Gets a pizza order when given the order number. Returns position index if found.
        """
        for index, pizza_order in enumerate(self.orders):
            if pizza_order.get_number() == order_number:
                return index

    def display_menu(self):
        """Displays the option menu to the user via print to console, and gets input
        """
        print()
        print("=" * 10, "Welcome to Pizza Palace", "=" * 10)
        print("1. Display orders.")
        print("2. Add new order.")
        print("3. Remove order.")
        print("4. Edit order.")
        print("5. Save orders.")
        print("6. Exit program.")
        print()
        self.choice = input("Selection> ")
        print()

    def display_orders(self):
        """Prints all orders to the console.
        """
        title = "** Order List **"
        print("*" * len(title))
        print(title)
        print("*" * len(title))

        # loop over each order and print order info
        for pizza_order in self.orders:3
            print(pizza_order)
            print("-" * len(title))

    def add_order(self):
        """Add an order to the orders list.
        """
        try:
            pizza_order = PizzaOrder()

            _number = int(input("Enter your order number: "))
            _type = input("Enter your order type: ")
            _amount = float(input("Enter your order amount: "))

            if self.get_order_from_list(_number) is not None:
                print("\nOrder number already exists! Try again.")
                return

            pizza_order.set_number(_number)
            pizza_order.set_type(_type)
            pizza_order.set_amount(_amount)

            self.orders.append(pizza_order)

        except ValueError:
            print("\nEntered invalid input! Try again.")

    def remove_order(self):
        """Remove an order from the orders list.
        """
        try:
            order_number = int(input("Which order number to remove: "))
            pos = self.get_order_from_list(order_number)
            if pos is not None:
                self.orders.pop(pos)
                print("\nRemoved order.")
            else:
                print("\nDid not find an order with that number! Try again.")

        except ValueError:
            print("\nEntered invalid input! Try again.")

    def edit_order(self):
        """Edit an order in the orders list.
        """
        try:
            order_number = int(input("Which order number to edit: "))
            pos = self.get_order_from_list(order_number)

            if pos is not None:
                try:
                    pizza_order = PizzaOrder()

                    _number = int(input("Enter your new order number: "))
                    _type = input("Enter your new order type: ")
                    _amount = float(input("Enter your new order amount: "))

                    pizza_order.set_number(_number)
                    pizza_order.set_type(_type)
                    pizza_order.set_amount(_amount)

                    self.orders.pop(pos)
                    self.orders.insert(pos, pizza_order)
                    print("\nChanged order.")

                except ValueError:
                    print("\nEntered invalid input! Try again.")

            else:
                print("\nDid not find an order with that number! Try again.")

        except ValueError:
            print("\nEntered invalid input! Try again.")

    def save_orders(self):
        """Saves all orders to `orders.txt`.
        """
        with open(f"{PATH}/dusti_orders.txt", 'w', encoding="utf-8") as f:
            for pizza_order in self.orders:
                f.write(f"{pizza_order.get_number()}, {pizza_order.get_type()}, {pizza_order.get_amount()}\n")

        print("Data saved.")

    def run(self):
        """The main loop for the application.
        """
        while True:
            self.display_menu()

            if self.choice == '1':
                self.display_orders()
            elif self.choice == '2':
                self.add_order()
            elif self.choice == '3':
                self.remove_order()
            elif self.choice == '4':
                self.edit_order()
            elif self.choice == '5':
                self.save_orders()
            elif self.choice == '6':
                break
            else:
                print("Option not available! Please try again.")

        print("Exiting program...")


if __name__ == '__main__':
    app = PizzaApp()
    app.run()
