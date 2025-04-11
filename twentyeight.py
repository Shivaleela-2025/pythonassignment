#1. Write a Python program to sum all the items in a list. 
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum_list(numbers))

