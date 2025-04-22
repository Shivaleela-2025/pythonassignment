#3.You have a dictionary. Ask the user to enter a key
#and display the corresponding value. Handle the KeyError.

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

key = input("Enter a key to look up (e.g., name, age, city): ")

try:
    print(f"The value for '{key}' is: {my_dict[key]}")
except KeyError:
    print(f"Error: '{key}' not found in the dictionary.")
