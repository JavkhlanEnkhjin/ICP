# 1.
# nested loop
def customer_heights():
    #creating height array
    height = []
    more = "y"
    #if input is y, meaning we need to add more elements
    while more == "y":
        x = int(input("Enter your height: "))
        #converting inch to centimeter and adding to array
        height.append(x * 2.54)
        more = input("Do you have a more numbers(y or n): ")
    print(height)
#customer_heights()

# list compehensions
def customer_heights1():
    height_in_inch = []
    more = "y"
    while more == "y":
        inch = int(input("Enter your height: "))
        height_in_inch.append(inch)
        #according to user input we add all the elements to the height_in_inch array
        more = input("Do you have a more numbers(y or n): ")
    #When the user is done adding the height in inches, we will convert the entire list
    #to centimeters using the for loop
    height_in_cm = [x * 2.54 for x in height_in_inch]
    print(height_in_cm)

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
    #For each character in the full name we added them to an array name
    for i in full_name:
        name.append(i)
    #We traverse the array by 2 steps skipping the 2nd character and then storing
    #the characters in string_a
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
    #open the input file
    infile = open("input.txt", 'r')
    line = infile.readline()
    #create dictionary
    words = dict()
    #create new file for output
    f = open("output.txt", "w")
    while line != "":
        #split each string by the space and store in array
        arr += [x.strip() for x in line.split(" ")]
        count = len(arr)
        #write every characters in line to output
        f.write(line)
        line = infile.readline()
    #each elements in the array, if it exists in dictionary we increment value by one,
    #if not we add it as a key
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

#file_read()
