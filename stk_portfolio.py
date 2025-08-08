# Stock Portfolio Tracker
# Internship Task 2 - CodeAlpha
# By: Om Malthane

# ==============================
# 1. Dictionary: Hardcoded stock prices
# ==============================
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

# Dictionary to store portfolio data
portfolio = {}

# ==============================
# 2. Input: Number of different stocks
# ==============================
while True:
    try:
        num_stocks = int(input("Enter number of different stocks you own: "))
        if num_stocks <= 0:
            print("⚠ Please enter a positive number.")
            continue
        break
    except ValueError:
        print("⚠ Please enter a valid number.")

# ==============================
# 3. Input: Stock name & quantity
# ==============================
for _ in range(num_stocks):
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()

    if stock_name not in stock_prices:
        print(f"⚠ {stock_name} not found in stock list. Skipping...")
        continue

    while True:
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity <= 0:
                print("⚠ Please enter a positive quantity.")
                continue
            break
        except ValueError:
            print("⚠ Please enter a valid number.")

    portfolio[stock_name] = quantity

# ==============================
# 4. Processing: Calculate total investment value
# ==============================
total_value = 0
print("\n----- Investment Summary -----")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty  # Basic Arithmetic
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print("\nTotal Investment Value: $", total_value)

# ==============================
# 5. Output (Optional): Save to file
# ==============================
save_option = input("\nDo you want to save this result? (y/n): ").lower()
if save_option == 'y':
    file_name = input("Enter file name (without extension): ")
    file_format = input("Choose format - txt or csv: ").lower()

    try:
        if file_format == "txt":
            with open(file_name + ".txt", "w") as f:
                for stock, qty in portfolio.items():
                    f.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
                f.write(f"\nTotal Investment Value: ${total_value}")
            print(f"✅ Data saved to {file_name}.txt")

        elif file_format == "csv":
            with open(file_name + ".csv", "w") as f:
                f.write("Stock,Quantity,Price,Total Value\n")
                for stock, qty in portfolio.items():
                    f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock] * qty}\n")
                f.write(f"Total,,,{total_value}")
            print(f"✅ Data saved to {file_name}.csv")

        else:
            print("⚠ Invalid format. Skipping save.")
    except Exception as e:
        print("⚠ Error saving file:", e)
