
students = []
all_subjects=set()
print("---Welcome to students Data organizer---")
print("This program will collect Data of the students.\nSuch as Add students, Display all students,Updating students Details etc.....")
while True:
    print("Select an option-->")
    print("1. Add students")
    print("2. Display all students")
    print("3. Update Students Details")
    print("4. Delete students")
    print("5. Display subject offered")
    print("6. Exit")

    option = int(input("Enter your choice: "))
# Add students
    if option == 1:
        print("Enter students details:")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        roll_no = int(input("Enter students ID: "))
        grade = input("Enter your grade: ")
        subjects = input("Enter your subjects: ")
        sid = input("Enter students email id: ")
        dob = input("Enter Date of birth: ")
        sub_set = subjects.split(",")
        sub_set=set(sub_set)
        id_dob=(roll_no,dob)
        all_subjects.update(sub_set)

        student = {
        "name": name,
        "age": age,
        "grade": grade,
        "email": sid,
        "subject_set":sub_set,
        "id_dob":id_dob
}
        students.append(student)
        print(students)
        print("Student added")
        print(all_subjects)
        
    elif option == 2:

        print("Display all students")

        if len(students) == 0:
            print("No data found")
        else:
            for s in students:
                print("ID:",s["id_dob"][0])
                print("Name:",s["name"])
                print("Age:",s["age"])
                print("Grade:",s["grade"])
                print("Subjects:",s["subject_set"])
    elif option == 3:
        print("Update students details")
        sid = int(input("Enter student ID: "))

    for s in students:
        if s["id_dob"][0] == sid:
            s["age"] = int(input("Enter new age: "))
            new_sub = input("Enter new subjects: ")
            s["subject_set"] = set(new_sub.split(","))  # This will return  subjects in the form of set
            print("Updated")
        
        elif option == 4:
            sid = int(input("Enter Student ID: "))

            for i in range(len(students)):
                if students[i]["id_dob"][0] == sid:
                    del students[i]
                    print("Deleted")
                    break
        elif option == 5:

            print("All subjects: ")
            print(all_subjects)

        elif option == 6:
            print("Thank you for visiting Students Data Organizer")
            break
        else:
            print("invalid choice")
            
    