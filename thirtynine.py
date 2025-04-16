#1.Create a dictionary with student names as keys and their marks as values. Allow the user to input a name
#and display the student's marks. If the student doesn't exist, show an appropriate message.
student_marks = {
    "Kunti": 85,
    "Gandhari": 92,
    "Subhadra": 78,
    "Hidimbe": 88
}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
