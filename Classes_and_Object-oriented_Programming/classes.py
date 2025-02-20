class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.annual_salary = None

    def increase_salary(self, percent):
        self.salary += self.salary * percent

    def __str__(self):
        return f"{self.name} is a {self.position} and earns ${self.salary: ,.2f}"

    def __repr__(self):
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.position)}, {repr(self.salary)})"
        )
    
    @property
    def salary(self):
        # return f"{${self.salary: ,.2f}"
        # logging.info("Someone accessed the salary attribute")
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 1000:
            raise ValueError("Minimun wage is $1000")
        self.annual_salary = None
        self._salary = new_salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self._salary * 12
        return self._annual_salary



employee1 = Employee("John Doe", 30, "Software Developer", 8566)

print(employee1.annual_salary)