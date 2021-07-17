current_savings = 0.0

r=0.04

#annual salary
annual_salary = float(input('Enter your annual salary: '))
#portion saved per month 
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
#total cost
total_cost = float(input('Enter the cost of your dream home: '))

semi_annual_raise = float(input('Enter the semi­annual raise, as a decimal: '))

portion_down_payment = 0.25*total_cost
month = 0
while (current_savings<portion_down_payment):
  monthly = annual_salary/12
  current_savings += ((current_savings*r)/12)
  current_savings += (portion_saved*monthly)
  month+=1;
  if(month%6==0):
    annual_salary+=(annual_salary*semi_annual_raise)
print('Number of months:', month)

