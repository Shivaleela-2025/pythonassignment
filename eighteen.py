# Function to Remove Specific Character from a String
#Write a function remove_char(s, char) that removes all occurrences of a specific character from a string.

#Input: A string s and a character char (e.g., "hello", 'l').
def remove_char(s, char):
    return s.replace(char, '')
print(remove_char("hello", 'l'))




