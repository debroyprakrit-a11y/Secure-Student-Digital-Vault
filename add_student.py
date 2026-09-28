def add_student(students):
    student_id = input("Enter student ID:")
    name = input("Enter student name:")
    course = input("Enter course name:")
    email = input("Enter email address:")
    marks = input("Enter marks:")
    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "email": email,
        "marks": marks
    }
    students.append(student)
    print("Student record saved!")