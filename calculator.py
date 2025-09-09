# Take input from user
price = int(input("Enter the price of the item (in cents, less than or equal to 100): "))

# Validate input
if price > 100 or price < 0:
    print("Invalid price! Please enter a value between 0 and 99 cents.")
else:
    change = 100 - price

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print(f"The price of your item is {price} cents, and your change is {100 - price} cents.")
    print("Here's the change that uses the fewest coins:")
    print(f"pennies: {pennies}")
    print(f"nickels: {nickels}")
    print(f"dimes: {dimes}")
    print(f"quarters: {quarters}")
