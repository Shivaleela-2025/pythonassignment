# 3. Customers who bought a product but never returned

all_customers = {"John", "Mary", "Steve", "Ana"}
returned_customers = {"Mary", "Ana"}

non_returning_customers = all_customers - returned_customers
print(non_returning_customers)
