#3. Write a Python program to find duplicate values from a list and display those.
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
numbers = [1, 1, 2, 3, 4, 4, 5, 1]
print("Duplicates:", find_duplicates(numbers))
