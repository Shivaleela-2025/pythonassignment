#2.Given a list of names, group them into a dictionary where the key is the first letter of each name
#and the value is a list of names that start with that letter.

names = ["Karna", "Arjuna", "Krishna", "Bhima", "Nakula", "Sahadeva"]
grouped_names = {}

for name in names:
    first_letter = name[0].upper()
    grouped_names.setdefault(first_letter, []).append(name)
print("Grouped names by first letter:")
for letter, group in grouped_names.items():
    print(f"{letter}: {group}")
