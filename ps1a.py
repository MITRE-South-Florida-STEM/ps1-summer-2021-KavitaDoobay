#received help from johanner 
current_savings = 0.0

r=0.04

#annual salary
annual_salary = float(input('Enter your annual salary: '))
#portion saved per month 
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
#total cost
total_cost = float(input('Enter the cost of your dream home: '))


portion_down_payment = 0.25*total_cost
ra = 0.0
monthly = annual_salary/12 + (annual_salary*ra)
month = 0
while (current_savings<portion_down_payment):
  current_savings += ((current_savings*r)/12)
  current_savings += (portion_saved*monthly)
  month+=1;

print('Number of months:', month)

