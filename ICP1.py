"""  ICP 1
Mohammad Abboud
Jawa Enkhjin
"""

""" 
1.
Python 3 syntax is simpler and easily understandable whereas 
Python 2 syntax is comparatively difficult to understand.
Python 3 default storing of strings is Unicode whereas 
Python 2 stores need to define Unicode string value with “u.”
Python 3 value of variables never changes whereas in Python 2 
value of the global variable will be changed while using it inside for-loop.
Python 3 exceptions should be enclosed in parenthesis while Python 2 
exceptions should be enclosed in notations.
Python 3 rules of ordering comparisons are simplified whereas Python 2 
rules of ordering comparison are complex.
Python 3 offers Range() function to perform iterations whereas, 
In Python 2, the xrange() is used for iterations.
"""


"""
2.
"""
def charDeleter():
    s = input("2. Please input the string: ")
    temp = ""
    for i in range(2, len(s), 1):
        temp += s[i]
    print(temp[::-1])


def addOperation():
    num1 = int(input("3. Please input 1st number: "))
    num2 = int(input("Please input 2nd number: "))
    print('Total: {}'.format(num1 + num2))

def createList():
    s = []
    s = [i for i in input("4. Please enter the name: ").split()]

    print(len(s))
    s.append(input("Please add new name: "))
    print(s)

def replaceWord():
    print(5.)
    text = "I love playing with python"
    print(text)
    print(text.replace("python", "pythons"))


#charDeleter()
#addOperation()
#createList()
#replaceWord()
