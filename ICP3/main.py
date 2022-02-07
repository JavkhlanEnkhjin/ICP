# 1. Classes and objects

class Employee:
    # b. create a class attribute to count the number of employees
    count_emp = 0

    # a. create a constructor to initialize
    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.balance = 0
        self.isEmployed = True
        Employee.count_emp += 1

    # e. create pay, fire, and isEmployed functions
    def pay(self):
        temp = self.balance + self.salary
        self.balance = temp

    def fire(self):
        self.salary = 0
        self.isEmployed = False

    def isEmployed_function(self):
        return self.isEmployed

# c. create a Full_time and Part_time employee classes and it should inherit
# the properties of the employee class
class Full_Employee(Employee):

    def __init__(self, id, name, department, salary, type):
        self.type = type
        Employee.__init__(self, id, name, department, salary)

    # d. create giveRaise method for full_time and part_time classes
    def giveRaise(self, salary):
        self.salary = salary + int(salary * 0.1)

class Part_Employee(Employee):

    def __init__(self, id, name, department, salary, type):
        self.type = type
        Employee.__init__(self, id, name, department, salary)

    def giveRaise(self, salary):
        self.salary = salary + int(salary * 0.05)

def start():
    temp, employee_list = [], []

    with open('input.txt', 'r') as f:
        temp = [name.rstrip().split(" ") for name in f]
    for i in range(len(temp)):
        if "NEW" in temp[i][0]:
            if temp[i][-1] == "F":
                employee_list.append(Full_Employee(temp[i][1], temp[i][2] + " " + temp[i][3], temp[i][4], int(temp[i][5]), temp[i][6]))
            else:
                employee_list.append(Part_Employee(temp[i][1], temp[i][2] + " " + temp[i][3], temp[i][4], int(temp[i][5]), temp[i][6]))

        elif "RAISE" in temp[i][0]:
            for j in employee_list:
                if j.id == temp[i][1] and len(temp[i]) == 2:
                    j.giveRaise(j.salary)
                elif j.id == temp[i][1] and len(temp[i]) == 3:
                    j.salary = j.salary + int(j.salary * (int(temp[i][2]) / 100))

        elif "PAY" in temp[i]:
            for j in employee_list:
                j.balance += j.salary

        elif "FIRE" in temp[i]:
            for j in employee_list:
                if j.id == temp[i][1]:
                    j.fire()

    #open text file to write output
    out = open("output.txt", "w")
    #iterate employee list and write data's in certain order to output text file
    for i in employee_list:
        out.write("{0}, ID {1}, {2}:".format(i.name, i.id, i.department) + '\n')
        out.write("Current salary: {}".format(i.salary) + '\n') if i.isEmployed_function() else out.write("Not employed with the company." + '\n')
        out.write("Pay earned to date: {}".format(i.balance) + '\n')
        out.write("Full time employee" + '\n') if i.type == "F" else out.write("Part time employee" + '\n')
        out.write('\n')
    #class instance employee count
    out.write("Total number of employee: {}".format(Employee.count_emp) + '\n')

    avgP_Count, avgF_Count = 0, 0
    avgP_Total, avgF_Total = 0, 0

    for i in employee_list:
        if i.type == "F":
            avgF_Count += 1
            avgF_Total += i.salary
        else:
            avgP_Count += 1
            avgP_Total += i.salary
    #based on employee type, get average salary. PS: one of the full time employee got fired, full time
    #employee's average salary is 2 employees salary divided by 3.
    out.write("Average Salary paid to all Full-time employee: {}".format(avgF_Total // avgF_Count) + '\n')
    out.write("Average Salary paid to all Part-time employee: {}".format(avgP_Total // avgP_Count) + '\n')
    out.close()
#to run the question 1 decomment below start() function
#start()


# 1.2 Optional question
class Car:
    def __init__(self, year, make, model):
        self.__year = year
        self.__make = make
        self.__model = model
    #creating private method to print attributes
    def __printinfo(self):
        print(self.__year, self.__make, self.__model)
    #creating public methods to call private method
    def printinfo(self):
        self.__printinfo()

Toyota = Car(2022, "Toyota", "LC 300")
#Toyota.printinfo()

# 2 Web scraping
import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
obj = BeautifulSoup(response.content, "html.parser")
print(obj.title)
images = obj.find_all('img')
for i in images:
    print(i.get('src'))


response = requests.get("https://en.wikipedia.org/wiki/Machine_learning")
plain_text = response.text
obj = BeautifulSoup(plain_text, "html.parser")
print(obj.title)
images = obj.find_all('a', {'class': 'image'})
for i in images:
    link = i.find('img')
    imglink = link.get('src')
    href = "https:" + imglink
    print(href)
