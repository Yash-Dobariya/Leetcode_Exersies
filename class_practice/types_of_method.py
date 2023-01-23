# Types of method
# 1. Instance Method
# 2. Class Method
# 3. Static Method

class Student:
    school = "xyz"

    # generator
    def __init__(self, name, rollno) -> None:
        self.name = name
        self.rollno = rollno

    # Instance Mehod(instance method use for instance variable)
    def get_student_info(self):
        print("Student name : ",self.name)
        print("Student rollno. : ",self.rollno)

    # Class Mthod (class use for Using static variable)
    @classmethod
    def get_school_info(cls):
        print("School name : ",cls.school)
    
    # Static Mehod(static method no using instance & static variable only use for general utility )
    @staticmethod
    def get_sum(a, b):
        return 'Sum is : ',a + b

s=Student("Yash", 123)
Student.get_student_info(s)
# Student.get_school_info()
print(Student.get_sum(1,2))
# print(*s.get_sum(1,2))