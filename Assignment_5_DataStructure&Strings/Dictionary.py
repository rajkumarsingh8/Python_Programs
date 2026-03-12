# student names are keys and their mar
students_marks = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Ethan": 76}

# user to input a student's name.
student_name = input(f"Enter the student's name: ")

normalized_name = (
    student_name.capitalize()
)  # By mistake end user enters the name in small caps

if normalized_name in students_marks:
    print(f"{normalized_name}'s marks: {students_marks[normalized_name]}")
else:
    print("Student not found")
