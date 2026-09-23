print("SECURE STUDENT DIGITAL VAULT")
print("Welcome to the Secure Student Digital Vault")
correct_password = "VIT Digital @1456"
attempts = 0
max_attempt= 3
access_granted = False
students =[]
while attempts < max_attempt:
    password = input("Enter your password:")
    if password == correct_password:
     print("Login Successful!")
     access_granted = True
     break
    else:
        print("Incorrect Password")
        attempts +=  1
if access_granted:
    print("Login successful!")

    while True:
        print("MAIN MENU")




        print("1.Add Student")
        print("2.View Student")
        print("3.View All Students")
        print("4.Student Statistics")
        print("5.Logout")
        choice = input("Enter your choice:")
        print("You selected option:", choice)

        if  choice == "1":
            student_id = input("Enter student ID:")
            name = input("Enter student name:")
            course =input("Enter course name:")
            email = input("Enter email address:")
            marks = input("Enter marks:")
            student ={
            "id": student_id,
            "name": name,
            "course": course,
            "email": email,
            "marks": marks
            }
            students.append(student)
            print("Student record saved!")

        elif choice == "2":
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

        elif choice == "3":
            if len(students) == 0:
                print("No student was found!")
            else:
                print("All Student Details")
                for record in students:
                    print("Student ID:", record["id"])
                    print("Student Name:", record["name"])
                    print("Student Course:", record["course"])
                    print("Student Email:", record["email"])

        elif choice == "4":
            if len(students) == 0:
                print("No student was found!")
            else:
                print("Student Statistics")
                print("Total Students:", len(students))
                courses ={}
                for record in students:
                    course =record["course"]
                    if course in courses:
                        courses[course] += 1
                    else:
                        courses[course] = 1
                print("Students by Course:")
                for course in courses:
                    print(course, courses[course])
                total_marks = 0.0
                for record in students:
                    total_marks += float(record["marks"])
                average_marks = total_marks / len(students)
                print("Average Marks:", average_marks)


        elif choice == "5":
            print("Logging out")
            access_granted = False
            break






else:
    print("Access denied!")







