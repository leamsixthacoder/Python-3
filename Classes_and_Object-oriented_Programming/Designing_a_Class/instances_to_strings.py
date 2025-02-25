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
        return f"{self.name} is {self.age} years old and earns ${self.salary:,.2f}"

employee1 = Employee("Ji-Soo", 37, "Developer", 1200)
employee1.increase_salary(20)
print(employee1)