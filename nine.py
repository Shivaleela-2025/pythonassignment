#write a function count_vowels(s) that returns the number of vowels (a,e,i,o,u) in the given string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
string1 = "hello world"
print(count_vowels(string1))
string2 = "python"
print(count_vowels(string2))
string3 = "beautiful day"
print(count_vowels(string3))
