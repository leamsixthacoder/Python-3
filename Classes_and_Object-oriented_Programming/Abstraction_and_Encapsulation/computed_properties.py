# Abstraction means that class instances should hide implementation details; Users only need to have the interface.

# Encapsulation means that class instances should group related data and methods
# In other words, group related data and methods in one logical unit.
# Hidding of data attributes which are only used for internal implementation purposes.

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

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
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    #should macth the name of the getter propertie
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimun wage is $1000')
        self._annual_salary = None 
        self.__salary = salary
        
    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

# Now we make instances of the Employee class
employee1 = Employee("Ji-Soo", 37, "Developer", 1200)

# now i can't get access from outside of the class
print(employee1.__salary)

