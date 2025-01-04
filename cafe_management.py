# Define the menu items
menu = {
    "Burger": 60,
    "Pasta": 50,
    "Pizza": 40,
    "Salad": 30,
    "Fries": 20,
    "Coffee": 70
}

# Greet the customer
print("Welcome to our cafe! What would you like to order?")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

# Initialize total order amount
order_total = 0

# Get the first order
order_1 = input("\nEnter your order: ").capitalize()

# Check if the order is in the menu
if order_1 in menu:
    order_total += menu[order_1]
    print(f"The item '{order_1}' has been added to your order for Rs.{menu[order_1]}.")
else:
    print(f"Sorry, we don't have '{order_1}'. Please choose something from the menu.")

# Ask if the customer wants to order more
another_order = input("\nWould you like to order something else? (yes/no): ").lower()

if another_order == "yes":
    # Get the second order
    order_2 = input("Enter your second order: ").capitalize()
    if order_2 in menu:
        order_total += menu[order_2]
        print(f"The item '{order_2}' has been added to your order for Rs.{menu[order_2]}.")
    else:
        print(f"Sorry, we don't have '{order_2}'. Please choose something from the menu.")
elif another_order == "no":
    print("Thank you for your order!")
   # Apply discount if applicable
if order_total > 100:
        discount = order_total * 0.1  # 10% discount
        order_total -= discount
        print(f"A discount of Rs.{discount:.2f} has been applied to your order.")
# Print the total price
if order_total > 0:
    print(f"\nTotal price of your order is Rs.{order_total}.")
    print("It will take a few minutes to prepare your order. Thank you for your patience!")
else:
    print("\nSorry, we could not fulfill your order. Have a nice day!")
