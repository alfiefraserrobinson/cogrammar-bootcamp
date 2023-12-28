# List of items on the Menu
menu = [
    "Tea",
    "Green Tea",
    "Latte",
    "Cappucino",
    "Espresso",
    "Sandwich",
    "Panini",
    "Full English",
]

# Dictionary containing stock quantities for each item in 'menu'
stock = {
    "Tea": 200,
    "Green Tea": 50,
    "Latte": 200,
    "Cappucino": 200,
    "Espresso": 250,
    "Sandwich": 75,
    "Panini": 75,
    "Full English": 50,
}

# Dictionary containing prices for each item in 'menu'
price = {
    "Tea": 1.00,
    "Green Tea": 1.00,
    "Latte": 2.00,
    "Cappucino": 2.00,
    "Espresso": 1.50,
    "Sandwich": 5.00,
    "Panini": 6.00,
    "Full English": 8.00,
}

# Variable to contain total stock worth
total_stock_worth = 0

# 'for' loop to iterate over each item in 'menu'
for item in menu:
    # Calculate the value of each item in 'menu' by multiplying the price of the item by its stock value. This is done for each item in 'menu'
    item_value = stock[item] * price[item]
    # Add the value from the previous equation to to this pre-made variable
    total_stock_worth += item_value
# Print the result
print(f"Total Stock Worth: £{total_stock_worth}")
