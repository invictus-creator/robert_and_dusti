from os.path import dirname
from typing import Optional

PATH = dirname(__file__)


class PizzaOrderApp(object):
    """This class creates and maintains the file `orders.txt`. When the run method is called, the class will
    display a menu in the console for the user to choose an action. The user can do one of the following:
        - Display orders.
        - Add new order.
        - Remove order.
        - Edit order.
        - Save order.
        - Exit program.
    """

    def __init__(self):
        """Initialize class instance and attributes
        """
        self._choice = "placeholder"
        self._all_orders = list()
        self._pizza_order = dict()

    def set_amount(self, order_amount: float):
        """Sets the order amount.

        :param order_amount: A float number representing the dollar amount of the order.
        :type order_amount: float
        """
        self._pizza_order['amount'] = order_amount

    def set_type(self, order_type: str):
        """Sets the order type.

        :param order_type: A description of the pizza type, i.e. pepperoni.
        :type order_type: str
        """
        self._pizza_order['type'] = order_type

    def set_number(self, order_number: int):
        """Sets the order number.

        :param order_number: An integer number to identify the order.
        :type order_number: int
        """
        self._pizza_order['number'] = order_number

    def get_amount(self, order_number: int) -> Optional[float]:
        """Get the order amount.

        :param order_number: The number associated with the order.
        :type order_number: int
        :return: The dollar amount of the order.
        :rtype: float, None
        """
        for order in self._all_orders:
            if order['number'] == order_number:
                return order['amount']
        return None

    def get_type(self, order_number: int) -> Optional[str]:
        """Get the order type.

        :param order_number: The number associated with the order.
        :type order_number: int
        :return: The description of the pizza order.
        :rtype: str, None
        """
        for order in self._all_orders:
            if order['number'] == order_number:
                return order['type']
        return None

    def get_number(self, order_pos: int) -> Optional[int]:
        """Get the order number.

        :param order_pos: The index position for an order.
        :type order_pos: int
        :return: The number for the order.
        :rtype: int, None
        """
        if self._all_orders:
            return self._all_orders[order_pos]['number']
        else:
            return None

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
        self._choice = input("Selection> ")
        print()

    def display_orders(self):
        """Prints all orders to the console.
        """
        title = ("** Order List **")
        print("*" * len(title))
        print(title)
        print("*" * len(title))

        # loop over each order and print order info
        for order in self._all_orders:
            print(f"Order number: {order['number']}")
            print(f"Order type: {order['type']}")
            print(f"Order amount: {order['amount']}")
            print("-" * len(title))

    def add_order(self):
        """Add an order to the orders list.
        """
        try:
            self._pizza_order = {}
            self._pizza_order['number'] = int(input("Enter your order number: "))
            self._pizza_order['type'] = input("Enter your order type: ")
            self._pizza_order['amount'] = float(input("Enter your order amount: "))
            self._all_orders.append(self._pizza_order)

        except ValueError:
            self._pizza_order = {}
            print("\nEntered invalid input! Try again.")

    def remove_order(self):
        """Remove an order from the orders list.
        """
        try:
            order_number = int(input("Which order number to remove: "))
            pos = None
            for index, order in enumerate(self._all_orders):
                if order['number'] == order_number:
                    pos = index

            if pos is not None:
                self._all_orders.pop(pos)
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
            pos = None
            for index, order in enumerate(self._all_orders):
                if order['number'] == order_number:
                    pos = index
                    break

            if pos is not None:
                try:
                    self._pizza_order = {}
                    self._pizza_order['number'] = int(input("Enter your new order number: "))
                    self._pizza_order['type'] = input("Enter your new order type: ")
                    self._pizza_order['amount'] = float(input("Enter your new order amount: "))

                    self._all_orders.pop(pos)
                    self._all_orders.insert(pos, self._pizza_order)
                    print("\nChanged order.")

                except ValueError:
                    self._pizza_order = {}
                    print("\nEntered invalid input! Try again.")

            else:
                print("\nDid not find an order with that number! Try again.")

        except ValueError:
            print("\nEntered invalid input! Try again.")

    def save_orders(self):
        """Saves all orders to `orders.txt`.
        """
        with open(f"{PATH}/orders.txt", 'w', encoding="utf-8") as f:
            for order in self._all_orders:
                f.write(f"{order['number']}, {order['type']}, {order['amount']}\n")

        print("\nData saved.")

    def run(self):
        """The main loop for the application.
        """
        while True:
            self.display_menu()

            if self._choice == '1':
                self.display_orders()
            elif self._choice == '2':
                self.add_order()
            elif self._choice == '3':
                self.remove_order()
            elif self._choice == '4':
                self.edit_order()
            elif self._choice == '5':
                self.save_orders()
            elif self._choice == '6':
                break
            else:
                print("Option not available! Please try again.")

        print("Exiting program...")


if __name__ == '__main__':
    app = PizzaOrderApp()
    app.run()
