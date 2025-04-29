from student import StudentDatabase, Student

stuData = StudentDatabase()

def show_student_data():
    stuData.show_students()

def enroll_student():
    name = input("Enter student name: ")
    department = input("Enter student department: ")
    student_id = int(input("Enter student ID: "))
    enrollment_status_input = input("Is the student enrolled? (yes/no): ").lower()

    for student in stuData.student_list:
        if student.get_student_id() == student_id:
            print(f"Student with ID {student_id} already exists. Enrollment failed.")
            return

    if enrollment_status_input == 'yes':
        is_enrolled = True
    else:
        is_enrolled = False

    new_student = Student(name, department, student_id, is_enrolled)
    stuData.add_student(new_student)
    print(f"Student {name} added successfully!")

def drop_student():
    student_id = int(input("Enter student ID to drop: "))
    for student in stuData.student_list:
        if student.get_student_id() == student_id:
            student.drop_student()
            print(f"Student {student.get_name()} dropped successfully!")
            return
    print("Student not found!")

while True:
    print("Welcome to the Student Management System")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        show_student_data()
    elif choice == 2:
        enroll_student()
    elif choice == 3:
        drop_student()
    else:
        break