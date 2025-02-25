class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)

    def info(self):
        print(f"{self.name} is {self.age} years old and earns ${self.salary:,.2f}")

employee1 = Employee("Ji-Soo", 37, "Developer", 1200)
employee1.increase_salary(20)
employee1.info()