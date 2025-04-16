#4.Create a contact book using a dictionary where the name is the key and
#phone number is the value. Allow the user to input a name and phone number.
#If the name exists, update the number; otherwise, insert a new contact.
contacts = {
    "Karan": "123-456-7890",
    "Arjun": "987-654-3210"
}
name = input("Enter contact name: ")
phone = input("Enter phone number: ")
if name in contacts:
    print(f"Updating {name}'s number.")
else:
    print(f"Adding new contact for {name}.")
contacts[name] = phone
print("Updated contact book:")
for name, number in contacts.items():
    print(f"{name}: {number}")
