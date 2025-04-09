#write a function is palindrome(s) that returns True if the input string s is a palindrome(reads the same forward and backward) and false otherwise
def is_palindrome(s):
    s=s.replace(" "," ").lower()
    return s==s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("racecar"))
