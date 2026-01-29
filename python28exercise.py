from os.path import exists
from python0test import function_y
from sys import argv
script,python0test = argv
print(f"Firstly,we need to understand test file {exists(python0test)} exists.")
print("This is a math script.")
print("Please tell me your name.")
name = input("name:>>>")
print("Welcome",name)
print("Which intnumber do you lile?")
number = int(input("number:"))
def add(f1):
    print(f"add: {f1} + {f1}")
    return f1 + f1
def subtract(f2):
    print(f"subtract: {f2} - {f2}")
    return f2 - f2
def multiply(f3):
    print(f"multiply: {f3} * {f3}")
    return f3 * f3
def divide(f4):
    print(f"divide: {f4} / {f4}")
    return f4 / (f4 +1)
x = divide(multiply(subtract(add(number))))
x += 1
y = function_y(x)
print(x)
print(y)
print(f"Yeah!I love you.","Or I can say that:",name,y)