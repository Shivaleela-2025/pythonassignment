#1.Write a Python program to generate an invoice for a customer using their name, product, and price details.
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))

print("\n--- INVOICE ---")
print(f"Customer: {customer_name}")
print(f"Product: {product_name}")
print(f"Price: ₹{price:.2f}")
print("Thank you for your purchase!")
