#3.Write a Python program to find the sum of digits of a number using a while loop.

num = int(input("Enter a number: "))
sum_of_digits = 0

while num > 0:
    digit = num % 10         
    sum_of_digits += digit   
    num = num // 10          
print("Sum of digits:", sum_of_digits)


