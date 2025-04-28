class StudentDatabase:
    def __init__(self):
        self.student_list = []
    
    def add_student(self, student):
        self.student_list.append(student)

    def show_students(self):
        if not self.student_list:
            print("No students here")
        else:
            for student in self.student_list:
                print(f"Name: {student.name} , ID: {student.student_id}")

class Student:
    def __init__(self, name, department, student_id, is_enrolled):
        self.name = name
        self.department = department
        self.student_id = student_id
        self.is_enrolled = is_enrolled
    
    def add_student(self, student):
        self.student_list.append(student)

    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f"{self.name} successfully enrolled")
        else:
            print(f"{self.name} already enrolled")

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print(f"{self.name} has dropped out")
        else:
            print(f"{self.name} is not enrolled")
    
    def view_student_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")

        if self.is_enrolled:
            status = "Enrolled"
        else:
            status = "Not Enrolled"

        print(f"Enrollment Status: {status}")

stu1 = Student("Rahim", "EEE", 125, True)
stuData = StudentDatabase()
stuData.add_student(stu1)

stu1.enroll_student()
stu1.view_student_info()