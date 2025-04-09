#Function to Count Occurrences of a Character in a String
#Write a function count_char_occurrences(s, char) that counts how many times a specific character char appears in the string s.

#Input: A string s and a character char (e.g., "hello", 'l').
def count_char_occurrences(s, char):
    return s.count(char)
print(count_char_occurrences("hello", 'l')) 

