#4.Take a feedback string and count how many times the word “good” appears in it (case-insensitive).
# Count 'good' in Feedback
feedback = input("Enter your feedback: ")
count_good = feedback.lower().count("good")
print(f"\nThe word 'good' appeared {count_good} times.")
