# Setter and Getter method

class Student:

    # Setter Method
    def setname(self, name):
        self.name = name

    # Getter Method
    def getname(self):
        return self.name

    def setmarks(self, marks):
        self.marks = marks

    def getmarks(self):
        return self.marks


n = int(input("Enter student of number : "))
student = []
for i in range(n):

    s = Student()
    name = input("Enter student name : ")
    marks = int(input("Enter student mark : "))
    s.setname(name)
    s.setmarks(marks)
    student.append(s)

for  j in student:
    print("Hii ", s.getname())
    print("Your marks is : ", s.getmarks())
    print()