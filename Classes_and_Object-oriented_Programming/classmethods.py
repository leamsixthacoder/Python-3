from datetime import date
class Employee:
    minimum_wage = 1000
    
    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        cls.minimum_wage = new_wage
    
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)
    
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage/100)
        
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    #should macth the name of the getter propertie
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f'Minimun wage is {Employee.minimum_wage}')
        self.__salary = salary
        
        
print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)