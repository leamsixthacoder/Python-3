# Working with complex data types

# We need to get all the employees 

employee1 = ["John Doe", 30, 8566]
employee2 = ["Jane Doe", 35, 9000]

employees = [employee1, employee2]

for employee in employees:
    print(f"{employee[0]} is {employee[1]} years old and earns ${employee[2]:,.2f}")

# Working like this is not ideal because we have to remember the order of the elements in the list.

# Dictionary
employee1 = {
    "name": "John Doe",
    "age": 30,
    "salary": 8566
}

employee2 = {
    "name": "Jane Doe",
    "age": 35,
    "salary": 9000
}

# This is better because we can access the values by their keys.
employees = [employee1, employee2]

for employee in employees:
    print(f"{employee['name']} is {employee['age']} years old and earns ${employee['salary']:,.2f}")


# You can also make things more organized by creating a function to create the employees
def init_employee(name, age, salary):
    return {
        "name": name,
        "age": age,
        "salary": salary
    }

employee3 = init_employee("John Doe", 30, 8566)
employee4 = init_employee("Jane Doe", 35, 9000)

# Know we can make complex operations with the data

def increase_salary(employee, percent):
    employee["salary"] += employee["salary"] * (percent / 100)

def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old and earns ${employee['salary']:,.2f}")

employees = [employee3, employee4]

for employee in employees:
    employee_info(employee)