#3.Build a simple inventory system where each item and its quantity is
#stored in a dictionary. Ask the user to enter an item name and quantity to sell.
#Update the dictionary and show the remaining stock or a message if there's not enough.
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 7
}
item = input("Enter item name to sell: ").lower()
quantity = int(input("Enter quantity to sell: "))
if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"{quantity} {item}(s) sold. Remaining stock: {inventory[item]}")
    else:
        print(f"Not enough {item}s in stock. Only {inventory[item]} available.")
else:
    print("Item not found in inventory.")
