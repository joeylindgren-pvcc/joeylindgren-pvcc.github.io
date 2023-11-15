import datetime

def calculate_cost(item_count, item_price):
    return item_count * item_price

def generate_receipt(pizza_size, num_pizzas, num_drinks, num_breadsticks):
    # Prices
    pizza_prices = {'S': 9.99, 'M': 12.99, 'L': 17.99, 'X': 21.99}
    drink_price = 3.99
    breadstick_price = 6.99
    sales_tax_rate = 0.055  # 5.5%

    # Calculations
    pizza_cost = calculate_cost(num_pizzas, pizza_prices[pizza_size])
    drink_cost = calculate_cost(num_drinks, drink_price)
    breadstick_cost = calculate_cost(num_breadsticks, breadstick_price)
    
    subtotal = pizza_cost + drink_cost + breadstick_cost
    sales_tax_amount = subtotal * sales_tax_rate
    total = subtotal + sales_tax_amount

    # Receipt Details
    current_datetime = datetime.datetime.now()
    print("\nPalermo Pizza Company Receipt")
    print(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
    print("--------------------------------------------------")

    # Order Details
    print(f"Pizza Size: {pizza_size}")
    print(f"Number of Pizzas: {num_pizzas}")
    print(f"Number of Drinks: {num_drinks}")
    print(f"Number of Breadsticks: {num_breadsticks}")
    print("--------------------------------------------------")

    # Costs
    print(f"Pizza Cost: ${pizza_cost:.2f}")
    print(f"Drink Cost: ${drink_cost:.2f}")
    print(f"Breadstick Cost: ${breadstick_cost:.2f}")
    print("--------------------------------------------------")

    # Total Costs
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (5.5%): ${sales_tax_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    # User Input
    pizza_size = input("Enter Pizza Size (S, M, L, X): ").upper()
    num_pizzas = int(input("Enter Number of Pizzas: "))
    num_drinks = int(input("Enter Number of Drinks: "))
    num_breadsticks = int(input("Enter Number of Breadsticks: "))

    # Generate and Display Receipt
    generate_receipt(pizza_size, num_pizzas, num_drinks, num_breadsticks)