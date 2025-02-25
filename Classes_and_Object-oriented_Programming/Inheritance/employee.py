 # Inheritance and Polymorphism. The key to writing maintainable code is to keep it DRY as possible. 
 # DRY stands for Don't Repeat Yourself.
class Employee:
    __slots__ = ("name", "age", "salary")
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent): 
        self.salary += self.salary * (percent / 100)
