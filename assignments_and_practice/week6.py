import copy

class Order:  # define Order class

    def __init__(self) :
        # define variables
        self._order_amount = 0
        self._order_type = ''
        self._order_number = 0

    def set_order_amount(self, order_amount):
        self._order_amount = order_amount

    def get_order_amount(self):
        return self._order_amount

    def set_order_type(self, order_type):
        self._order_type = order_type

    def get_order_type(self):
        return self._order_type

    def set_order_number(self, order_number):
        self._order_number = order_number

    def get_order_number(self):
        return self._order_number

    def display_order(self):
        print('    Order number: %s' % self._order_number)
        print('    Order type: %s' % self._order_type)
        print('    Order amount: %s' % self._order_amount)

def display_menu():
    print ("""**********Welcome to Pizza Palace - Class Demo***********
    1. Display Orders 
    2. Add Order
    3. Remove Order   
    4. Edit Order    
    5. Save Order
    6. Exit program    
    """)

def add_order(orders):
    order_number = int(input('Enter order number: '))  # ask user to prompt order number
    # check order_number exist in order list or not
    found = False
    for element in orders:
        if element.get_order_number() == order_number:  # find order to remove
            found = True
            break
        # end if
    # end for
    if found:
        print ('The order number %s already exist in order list' % order_number)
        return None
    # else
    order_type = input('Enter order type: ')  # ask user to prompt order number
    order_amount = int(input('Enter order amount: '))  # ask user to prompt order number
    order = Order()
    order.set_order_type(order_type)
    order.set_order_number(order_number)
    order.set_order_amount(order_amount)
    order.display_order()
    orders.append(order)

def remove_order(orders):
    order_number = int(input('Enter order number to remove: '))  # ask user to prompt order number to remove from list of orders
    index = -1
    id = 0
    for order in orders:
        if order.get_order_number() == order_number:  # find order to remove
            index = id
            break
        id += 1
    # end for
    if index >= 0:
        del orders[index]
    else:
        print ('Can not found order %s' % order_number)
    # end if


def edit_order(orders):
    order_number = int(input('Enter order number to edit: '))  # ask user to prompt order number to edit
    found = False
    for order in orders:
        if order.get_order_number() == order_number:  # find order to edit
            found = True
            new_order_type = input('Enter new order type: ')  # ask user to prompt order number
            new_order_amount = int(input('Enter new order amount: '))  # ask user to prompt order number
            order.set_order_type(new_order_type)
            order.set_order_amount(new_order_amount)
        # end if
    # end for
    if not found:
        print ('Can not found order %s' % order_number)
    # end if

def display_orders(orders):
    if len(orders) == 0:
        print ('List of order is empty')
    else:
        print ('Displaying order list:')
        for order in orders:
            order.display_order()
        # end for
    # end if

def save_orders(orders):
    file = open('orders.txt', 'w')
    for order in orders:
        file.write('Order number: %s' % order.get_order_number())
        file.write('Order type: %s' % order.get_order_type())
        file.write('Order amount: %s' % order.get_order_amount())
    # end for
    file.close()

if __name__ == '__main__':
    orders = []  # create list of order
    while True:
        display_menu()
        print ('Choose a menu option from 1-5 or 6 to exit the program:')
        choice = int(input())  # get choice
        if choice == 6:  # exit program
            break
        # else
        if choice == 1:
            display_orders(orders)
        elif choice == 2:
            add_order(orders)
        elif choice == 3:
            remove_order(orders)
        elif choice == 4:
            edit_order(orders)
        elif choice == 5:
            save_orders(orders)

