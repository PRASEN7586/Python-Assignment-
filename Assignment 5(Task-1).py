
def get_student_marks():
    """
    Creates a dictionary of student marks, asks for a student's name,
    and displays their marks or a 'not found' message.
    """

    # 1. Create a dictionary where student names are keys and their marks are values.
    student_marks = {
        "Prasen": 85,
        "Rahim": 72,
        "Akash": 90,
        "Abhi": 65,
        "Raj": 78
    }

    # 2. Ask the user to input a student's name.
    student_name = input("Enter the student's name: ")

    # 3. Retrieve and display the corresponding marks.
    # 4. If the student's name is not found, display an appropriate message.
    if student_name in student_marks:
        marks = student_marks[student_name]
        print(f"{student_name}'s marks: {marks}")
    else:
        print("Student not found.")

# Call the function to execute the program
get_student_marks()