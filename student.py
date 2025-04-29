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
                print(f"Name: {student.get_name()} , ID: {student.get_student_id()}, Enrollment Status: {student.is_enrolled()}")

class Student:
    def __init__(self, name, department, student_id, is_enrolled):
        self.__name = name
        self.__department = department
        self.__student_id = student_id
        self.__is_enrolled = is_enrolled
    
    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id
    
    def is_enrolled(self):
        if self.__is_enrolled:
            return "Yes"
        else:
            return "No"
    
    def add_student(self, student):
        self.student_list.append(student)

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"{self.__name} successfully enrolled")
        else:
            print(f"{self.__name} already enrolled")

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"{self.__name} has dropped out")
        else:
            print(f"{self.__name} is not enrolled")
    
    def view_student_info(self):
        print(f"Name: {self.__name}")
        print(f"Student ID: {self.__student_id}")
        print(f"Department: {self.__department}")

        if self.__is_enrolled:
            status = "Enrolled"
        else:
            status = "Not Enrolled"

        print(f"Enrollment Status: {status}")

stu1 = Student("Rahim", "EEE", 125, True)
stuData = StudentDatabase()
stuData.add_student(stu1)

stu1.enroll_student()
stu1.view_student_info()