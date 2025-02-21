# A class is a blueprint for objects. 
# It defines a data type that contains object attributes and functions that operate on that data.

# Everything in python is an object that are instances of class.
# this allow python to be a dynamicly typed language.
# s = "Hello" is an object of the class str
# l = [1, 2, 3] is an object of the class list
# d = {"name": "John"} is an object of the class dict
# you don't have to define the class of the object, python does it for you.

class newClass:
    pass

# So just by calling an empty class like this, you're actually allocating space for a new object in memory
n = newClass()

# In essence, objects in Python are like really powerful dictionaries.
# Each object actually uses an internal dictionary to store its data attributes.

# So this will print a empty dictionary 
print(n.__dict__)

# Class Functions for Constructing and Object
# 1. __new__ : Allocate memory for a new object and send it to the __init__ function.
# 2. __init__ : Recieve a new object from the __new__ function as a "self" parameter.

class Employee:
    def __init__(self):
        self.__dict__['name'] = "Ji-Soo"
        self.__dict__['age'] = 37
        self.__dict__['position'] = "Developer"
        self.__dict__['salary'] = 1200

e = Employee()
print(e.__dict__)