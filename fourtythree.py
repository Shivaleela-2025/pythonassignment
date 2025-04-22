#1.Write a program that asks the user for a list index and prints the value at
#that index from a predefined list. Handle the IndexError and ValueError exceptions.

my_list = ['apple', 'banana', 'cherry', 'date']

try:
    index = int(input("Enter an index (0-3) to access an item from the list: "))
    print(f"The item at index {index} is: {my_list[index]}")
except IndexError:
    print("Error: Index out of range. Please enter a valid index between 0 and 3.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
