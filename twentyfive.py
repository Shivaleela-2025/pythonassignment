#3.Write a program that removes extra spaces from a user-entered message.
# Remove Extra Spaces
message = input("Enter your message: ")
cleaned_message = ' '.join(message.split())
print("\nCleaned Message:")
print(cleaned_message)
