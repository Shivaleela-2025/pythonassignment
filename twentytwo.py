#3. Calculate the Sum of Even Numbers
#Write a program to calculate the sum of all even numbers in a given range.
#Input: Two integers start and end.
#Input: start = 1, end = 10

def sum_even_numbers(start, end):
    even_sum = sum(i for i in range(start, end + 1) if i % 2 == 0)
    print(f"Sum of even numbers from {start} to {end}: {even_sum}")
start = 1
end = 10
sum_even_numbers(start, end)
