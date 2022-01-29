# 1.
# nested loop
def customer_heights():
    height_in_cm = []
    more = "y"
    while more == "y":
        x = int(input("Enter your height: "))
        height_in_cm.append(x * 2.54)
        more = input("Do you have a more numbers(y or n): ")
    print(height_in_cm)

# list compehensions
def customer_heights1():
    height_in_inch = []
    more = "y"
    while more == "y":
        inch = int(input("Enter your height: "))
        height_in_inch.append(inch)
        more = input("Do you have a more numbers(y or n): ")
    height_in_cm = [x * 2.54 for x in height_in_inch]
    print(height_in_cm)

#customer_heights()
#customer_heights1()

# 2.
# user name
def user_name():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    full_name = first_name + " " + last_name
    return full_name

def string_alternative(full_name):

    name = []
    string_a = ""
    for i in full_name:
        name.append(i)
    for i in range(0, len(name) - 1, 2):
        string_a += name[i]
    print(string_a)

#string_alter = user_name()
#print(string_alter)
#string_alternative(string_alter)

# 3.
# input text
def file_read():
    count = 0
    arr = []
    infile = open("input.txt", 'r')
    line = infile.readline()
    words = dict()
    f = open("output.txt", "w")
    while line != "":
        arr += [x.strip() for x in line.split(" ")]
        count = len(arr)
        f.write(line)
        line = infile.readline()
    for i in arr:
        if i not in words:
            words[i] = 1
        else:
            words[i] += 1

    f.write("Word_Count: " + str(count) + '\n')
    f.write("Python: " + str(words["Python"]) + '\n')
    f.write("Deep: " + str(words["Deep"]) + '\n')
    f.write("Learning: " + str(words["Learning"]) + '\n')
    f.write("Course: " + str(words["Course"]))
    f.close()

file_read()