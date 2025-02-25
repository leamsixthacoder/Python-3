class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)

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
        
    # Getter
    def get_salary(self):
        # return f"{${self.salary: ,.2f}"
        # logging.info("Someone accessed the salary attribute")
        return self.salary
    
    # Setter
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimun wage is $1000')
        self.salary = salary

# Now we make instances of the Employee class
employee1 = Employee("Ji-Soo", 37, "Developer", 1200)

print(employee1.name)