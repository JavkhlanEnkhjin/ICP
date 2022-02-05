# 1. Classes and objects
class Employee:

    count_emp = 0

    def __init__(self, id, name, department, salary, emp_type):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.balance = 0
        self.isEmployed = True
        self.emp_type = emp_type

    def pay(self):
        temp = self.balance + self.salary
        self.balance = temp

    def fire(self, id):
        self.salary = 0
        self.isEmployed = False

    def isEmployed(self):
        return self.isEmployed



    def showEmployee(self):
        print('{0} {1} {2} {3} {4} {5}'.format(self.id, self.name, self.department, self.salary, self.balance, self.emp_type))

class Full_Employee(Employee):
    def __init__(self, id, name, department, salary, emp_type):
        Employee.__init__(self, id, name, department, salary, emp_type)
        self.type = type
    def giveRaise(self, salary):
        temp = salary * 0.1
        self.salary = temp

class Part_Employee(Employee):
    def __init__(self, id, name, department, salary, balance, emp_type):
        Employee.__init__(self, id, name, department, salary, balance, emp_type)
    def giveRaise(self, salary):
        temp = salary * 0.05
        self.salary = temp

e1 = Employee(1, "Jawa", "IT", 10000, "F")
e1.showEmployee()

e1.pay()
e1.pay()
e1.pay()

e1.showEmployee()




