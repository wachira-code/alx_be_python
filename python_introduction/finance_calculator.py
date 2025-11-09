#Enter monthly income and monthly expenses
monthly_income = int(input("Enter your monthly income "))
monthly_expenses = int(input("Enter your total monthly expenses "))

#Calculate monthly savings and projected savings for one year
monthly_savings = monthly_income - monthly_expenses
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#Display the results
print(f"Your monthly savinfgs are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")