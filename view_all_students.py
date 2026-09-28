def view_all_students(students):
    if len(students) == 0:
        print("No student was found!")
    else:
        print("All Student Details")
        for record in students:
            print("Student ID:", record["id"])
            print("Student Name:", record["name"])
            print("Student Course:", record["course"])
            print("Student Email:", record["email"])