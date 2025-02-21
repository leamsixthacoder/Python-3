from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        print('Current employees:')
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print('---------------------------------')
    
    def pay_employee(self):
        print('Paying employees:')
        for employee in self.employees:
            paycheck = employee.calculate_paycheck()
            print(f"Paycheck for {employee.fname} {employee.lname}")
            print(f"Amount: ${paycheck:,.2f} USD")
        print('---------------------------------')



def main():
    company = Company()
    employee1 = SalaryEmployee("John", "Doe", 50000)
    company.add_employee(employee1)
    employee2 = HourlyEmployee("Jane", "Smith", 25,50)
    company.add_employee(employee2)
    employee3 = CommissionEmployee("Alice", "Johnson", 30000, 5, 200)
    company.add_employee(employee3)

    company.display_employees()
    company.pay_employee()

if __name__ == "__main__":
    main()