from employee import Employee
class Developer(Employee):
    __slots__ = ("framework")
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

