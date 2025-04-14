# Student data will be stored as a list of tuples
# Each tuple: (Name, Roll Number, (Marks1, Marks2, Marks3), Grade)
# 1. Create Students
students = []

def create_students():
    global students
    students = [
        ("Shree", 101, (85, 90, 88), "A"),
        ("Bhaggu", 102, (78, 82, 80), "B"),
        ("Charlie", 103, (92, 95, 94), "A"),
    ]

# 2. Display All Students
def display_students():
    print("\nAll Student Records:")
    for student in students:
        print(student)

# 3. Add a New Student
def add_student(name, roll_no, marks, grade):
    student = (name, roll_no, marks, grade)
    students.append(student)
    print(f"\nStudent {name} added successfully.")

# 4. Search for a Student
def search_student(roll_no):
    print(f"\nSearching for Roll Number: {roll_no}")
    for student in students:
        if student[1] == roll_no:
            print("Student Found:", student)
            return
    print("Student not found.")

# 5. Calculate Total Marks
def calculate_total_marks():
    print("\nTotal Marks for Each Student:")
    for student in students:
        total = sum(student[2])
        print(f"{student[0]} (Roll {student[1]}): Total Marks = {total}")

# 6. Update Grades
def update_grade(roll_no, new_grade):
    global students
    for i, student in enumerate(students):
        if student[1] == roll_no:
            updated_student = (student[0], student[1], student[2], new_grade)
            students[i] = updated_student
            print(f"\nGrade updated for Roll Number {roll_no}.")
            return
    print("Student not found.")

# 7. Remove a Student
def remove_student(roll_no):
    global students
    for i, student in enumerate(students):
        if student[1] == roll_no:
            students.pop(i)
            print(f"\nStudent with Roll Number {roll_no} removed.")
            return
    print("Student not found.")

# Demo usage
create_students()
display_students()
add_student("David", 104, (75, 80, 78), "B")
search_student(102)
calculate_total_marks()
update_grade(103, "A+")
remove_student(101)
display_students()
