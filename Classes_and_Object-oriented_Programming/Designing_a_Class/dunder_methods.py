class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    # str method is to return a readable string representation of an object, usually for the end user or for debugging and development
    def __str__(self):
        return f"{self.name} is {self.age} years old, Employee us a {self.position} and earns ${self.salary:,.2f}"
    # This method should return the official string representation of an object. which is meant to be used by developers and not by the end users.
    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.position)}, {repr(self.salary)})"
        )
    
    # Dunder Methods: Special "magic" methods that start and end with the double underscore. Usually invoked by a special syntax.
    def __add__(self, other_employee):
        # E. g. combines their age and returns a new Employee
        return Employee("New", self.age + other_employee.age, "dev", 2000)

employee1 = Employee("Ji-Soo", 37, "Developer", 1200)
employee1.increase_salary(20)
print(eval(repr(employee1)))