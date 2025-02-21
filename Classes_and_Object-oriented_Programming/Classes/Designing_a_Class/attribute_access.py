class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary


# Now we make instances of the Employee class
employee1 = Employee("Ji-Soo", 37, "Developer", 1200)

print(employee1.name)