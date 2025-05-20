from customer import Customer
from coffee import Coffee

class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise Exception("coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise Exception("price must be a float")
        if price < 1.0 or price > 10.0:
            raise Exception("price must be between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price

    def customer(self):
        return self._customer

    def coffee(self):
        return self._coffee

    def price(self):
        return self._price

    customer = property(customer)
    coffee = property(coffee)
    price = property(price)