'''
PROBLEM SET 1

Part B: Saving, with a raise 

Background

In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and clearly you are going to be worth more to your company over time! So we are going to build on your solution to Part A by factoring in a raise every six months.
In ps1b.py , copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 2. After the 6 month the 9 month, the 18 month, and so on.
month, increase your salary by that percentage. Do the same after the 12 th
th
Write a program to calculate how many months it will take you save up enough money for a down payment. LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables: 1. The starting annual salary (annual_salary)
22. The percentage of salary to be saved (portion_saved) 3. The cost of your dream home (total_cost) 4. The semi­annual salary raise (semi_annual_raise)'''

annual_salary = round(float(input("Enter your annual salary: ")), 3) 
portion_saved = round(float(input("Enter a percent of your salary to save, as a decimal: ")), 3)
total_cost = round(float(input("Enter the cost of your dream house: ")), 3)
semi_annual_raise = round(1.00 + float(input("Enter the semi-annual raise, as a decimal: ")), 3)

# annual_salary = 80000.00 
# portion_saved = 0.15
# total_cost = 1000000.00
# semi_annual_raise = 1.03

portion_down_payment = 0.25
annual_return = 0.04
total_months = 0
current_savings = 0
monthly_salary = annual_salary/12
needed_down_payment = total_cost*portion_down_payment


while current_savings < needed_down_payment:
    total_months += 1
    if total_months % 6 == 0:
        monthly_salary *= semi_annual_raise
    current_savings += monthly_salary*portion_saved + current_savings*annual_return/12
    

print(f"Number of months: {total_months}")
