class School:
    pass

class Student(School):
    pass

class Teacher(School):
    pass

class Admin(School):
    pass

class Classrooms(School):
    pass








































































































dua
 # Student data management system
students = []  # List to store student data

while True:
    # Display the menu to the user
    print("\nClassroom Student Data Management")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    # User input to choose an option
    choice = input("Enter your choice (1-4): ")

    # Check if choice is valid
    if choice == '1':
        # Add a new student
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        students.append({'name': name, 'roll_no': roll_no})
        print(f"Student {name} added successfully!")

    elif choice == '2':
        # View all students
        if len(students) == 0:
            print("No students added yet!")
        else:
            print("\nList of students:")
            for student in students:
                print(f"Name: {student['name']}, Roll No: {student['roll_no']}")

    elif choice == '3':
        # Search for a student
        search_roll_no = input("Enter roll number to search: ")
        found = False
        for student in students:
            if student['roll_no'] == search_roll_no:
                print(f"Student found: Name: {student['name']}, Roll No: {student['roll_no']}")
                found = True
                break  # Exit the loop once the student is found
        if not found:
            print("Student not found with this roll number.")

    elif choice == '4':
        # Exit the program
        print("Exiting the program...")
        break

    else:
        print("Invalid choice, please try again.")
