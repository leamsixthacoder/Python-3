"""

This relationship between classes is known as composition, 
and a lot of programmers actually use this kind of approach 
instead of using inheritance. The inheritance we talked about uses
"as" the is a relationship between classes, like the developer is an employee.
However, composition implements the so called "has" a relationship because employee has a project.

"""
from dataclasses import dataclass
@dataclass
class Project:
    name: str
    payment:int
    client: str
    
class Employee:
     def __init__(self, name, age, salary , project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project
    

p = Project("Django app", 20000, "Globomantics")
e = Employee("Ji-soo", 38, 1000, p)
print(e.project)