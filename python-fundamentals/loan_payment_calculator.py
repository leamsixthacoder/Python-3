# Get details of the loan
money_owned = float(input("Enter the amount of money you owe: ")) # $50,000
annual_interest_rate = float(input("Enter the annual interest rate: ")) # 3.5%
monthly_payment = float(input("Enter the monthly payment: ")) # $1,000
months = int(input("Enter the number of months: ")) # 12

# Calculate the monthly interest rate

monthly_rate = annual_interest_rate / 12 / 100

for i in range(months):

    # Calculate the monthly payment
    interest_paid = money_owned * monthly_rate

    # Add in the monthly interest
    money_owned = money_owned + interest_paid

    if(money_owned - monthly_payment < 0):
        print(f"Payment: {money_owned:.2f} of which {interest_paid:.2f} was interest")
        print(f"Your loan has been paid off! in {i + 1} months")
        break

    # Make payment
    money_owned = money_owned - monthly_payment

    # Display the monthly payment
    print(f"Payment: {monthly_payment:.2f} of which {interest_paid:.2f} was interest")
    print(f"Remaining balance: {money_owned:.2f}")


