class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise Exception("Coffee name must be at least 3 characters long")
        self._orders = []

    def get_name(self):
        return self._name

    name = property(get_name)

    def orders(self):
        return self._orders

    def customers(self):
        result = []
        for order in self._orders:
            if order.customer not in result:
                result.append(order.customer)
        return result

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if len(self._orders) == 0:
            return 0
        total = 0
        for order in self._orders:
            total += order.price
        return total / len(self._orders)