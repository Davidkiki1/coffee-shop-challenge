class Customer:
    def __init__(self, name):
        self.set_name(name)
        self._orders = []

    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name should be a string between 1 and 15 characters")

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def orders(self):
        return self._orders

    def coffees(self):
        coffee_list = []
        for order in self._orders:
            if order.coffee not in coffee_list:
                coffee_list.append(order.coffee)
        return coffee_list

    def create_order(self, coffee, price):
        from order import Order
        new_order = Order(self, coffee, price)
        self._orders.append(new_order)
        coffee._orders.append(new_order)
        return new_order