from customer import Customer
from coffee import Coffee

# Create some customers
john = Customer("John")
emma = Customer("Emma")

# Create some coffees
latte = Coffee("Latte")
cappuccino = Coffee("Cappuccino")

# Create some orders
# Prices must be floats between 1.0 and 10.0
order1 = john.create_order(latte, 3.5)
order2 = john.create_order(cappuccino, 4.0)
order3 = emma.create_order(latte, 2.5)

# Check how many orders each customer has
print("John's Orders:", john.orders())
print("Emma's Orders:", emma.orders())

# Check which coffees each customer has tried
print("John's Coffees:", [c.name for c in john.coffees()])
print("Emma's Coffees:", [c.name for c in emma.coffees()])

# Check how many people ordered each coffee
print("Latte Customers:", [c.name for c in latte.customers()])
print("Cappuccino Customers:", [c.name for c in cappuccino.customers()])

# Number of orders for each coffee
print("Latte order count:", latte.num_orders())
print("Cappuccino order count:", cappuccino.num_orders())

# Average price of each coffee
print("Latte average price:", latte.average_price())
print("Cappuccino average price:", cappuccino.average_price())