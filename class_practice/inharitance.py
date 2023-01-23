class Employee:

    def __init__(self,eno,ename,esalary) -> None:
        self.eno=eno
        self.ename = ename
        self.esalary=esalary

    def display(self):
        print("Employee number : ",self.eno)
        print("Employee name : ",self.ename)
        print("Employee name : ",self.esalary)

class Manager(Employee):

    def update_emp_salary(emp):
        emp.esalary = emp.esalary + 10000
        emp.display()

emp=Manager(101, 'Yash', 45000)
# print(emp.eno,emp.ename,emp.esalary)
Manager.update_emp_salary(emp)