from add_student import add_student
from view_student import view_student
from view_all_students import view_all_students
from student_statistics import student_statistics
from logout import logout
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
            add_student(students)

        elif choice == "2":
            view_student(students)

        elif choice == "3":
            view_all_students(students)

        elif choice == "4":
            student_statistics(students)

        elif choice == "5":
            logout()
            access_granted = False
            break


else:
    print("Access denied!")







