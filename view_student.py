def view_student(students):
    if len(students) == 0:
        print("No student was found")
    else:
        search_id = input("Enter student ID:")
        found_student = False
        for record in students:
            if record["id"] == search_id:
                print("Student Details")
                print("Student ID:", record["id"])
                print("Student Name:", record["name"])
                print("Student Course:", record["course"])
                print("Student Email:", record["email"])
                print("Student Marks:", record["marks"])
                found_student = True
                break
        if not found_student:
            print("No student with this ID was found!")
