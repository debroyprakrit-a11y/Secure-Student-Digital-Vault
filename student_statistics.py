def student_statistics(students):
    if len(students) == 0:
        print("No student was found!")
    else:
        print("Student Statistics")
        print("Total Students:", len(students))
        courses = {}
        for record in students:
            course = record["course"]
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
