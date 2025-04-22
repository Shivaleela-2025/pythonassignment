#2. Create a program to validate exam scores entered by the user. Use a custom exception to handle invalid scores.
#Create a custom exception class called InvalidScoreError that will be raised if:
#The score is less than 0.
#The score is greater than 100.
#Write a function called validate_score(score) that:
#Takes a score as input.
#Raises InvalidScoreError if the score is not in the valid range (0–100).
#Returns a success message if the score is valid.
#Use try-except blocks to:
#Catch the custom exception and print an error message.

class InvalidScoreError(Exception):
    pass
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Invalid score: {score}. Score must be between 0 and 100.")
    return f"Score {score} is valid."
try:
    score = float(input("Enter the exam score (0–100): "))
    result = validate_score(score)
    print(result)
except InvalidScoreError as e:
    print("Error:", e)
except ValueError:
    print("Error: Please enter a numeric value.")
