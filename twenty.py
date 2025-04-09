#1. Print a Pyramid Pattern of Stars:
#Write a program to print a pyramid pattern using stars (*).

#Input: An integer n representing the number of rows.

def print_pyramid(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
n = 5
print_pyramid(n)
