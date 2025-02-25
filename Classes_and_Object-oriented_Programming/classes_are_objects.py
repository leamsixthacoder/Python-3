
class Employee:
    minimum_wage = 1000
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
        
        
e = Employee("John Doe", 30,"Developer", 8566)
Employee.__dict__["increase_salary"](e, 20)