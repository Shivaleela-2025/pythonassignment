#2. Write a Python program to get the largest and smallest number from a list without builtin functions. 
def find_min_max(lst):
    min_val = lst[0]
    max_val = lst[0]
    for num in lst[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val
numbers = [4, 2, 9, 1, 5, 6]
minimum, maximum = find_min_max(numbers)
print("Smallest:", minimum)
print("Largest:", maximum)
