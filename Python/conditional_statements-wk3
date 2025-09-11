def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get inputs from user
price = float(input("Enter original price of item: "))
discount_percent = float(input("Enter discount percentage: "))

# Call function
final_price = calculate_discount(price, discount_percent)

# Print the result
print("Final price:", final_price)
