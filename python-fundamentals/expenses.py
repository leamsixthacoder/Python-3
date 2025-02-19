total = 0
expenses = []

num_expenses = int(input("Enter the number of expenses: "))
for i in range(num_expenses):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)

total = sum(expenses)

print(f"Total expenses: {total}")