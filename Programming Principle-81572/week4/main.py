from student import Student
from student_repository import save_students, load_students, find_student_by_id 

while True:
    print("\nStudent registery")
    print("1. Add student")
    print("2. Show all students")
    print("3. Find student by ID")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    match choice:
        case "1":
            student_id = input("Student ID: ").strip()
            name = input("Student Name: ").strip()
            course = input("Course: ").strip()

            if not student_id or not name or not course:
                print("A Student with that ID already exists.")
                continue
            existing_student = find_student_by_id(student_id)
            if existing_student is not None:
                print("A Student with that ID already exists.")
                continue
            
            student = Student(student_id, name, course)
            save_students([student])
            print("Student Saved.")
        case "2":
            students = load_students()

            if not students:
                print("No students saved yet.")
            else:
                print("\nSaved Students:")
                for student in students:
                    print(student)
        case "3":
            student_id = input("Enter Student ID to search: ").strip()
            student = find_student_by_id(student_id)

            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")

        case "4":
            print("Goodbye.")
            break

        case _:
            print("Invalid option. please choose 1,2,3 or 4.")


