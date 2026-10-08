#we need to import modules using package as a employee and in this modules methods are done to calculates tax salary and bonus
from employee.salary import calculate_salary
from employee.tax import calculate_tax
from employee.bonus import calculate_bonus


# values are given
basic = 30000
allowance = 5000

#here we create a object to call the methods in the modules
salary = calculate_salary(basic, allowance)
tax = calculate_tax(salary)
bonus = calculate_bonus(salary)


# to display the output
print("Basic Salary:", basic)
print("Allowance:", allowance)
print("Total Salary:", salary)
print("Tax:", tax)
print("Bonus:", bonus)