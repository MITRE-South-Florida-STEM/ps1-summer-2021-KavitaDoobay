class ps1c:
  start = 0;
  end = 10000;              
  steps = 0;
  annual_salary = float(input('Enter the starting salary: '))
  total_cost = 1000000.0
  semi_annual_raise = 0.07
  portion_down_payment = 0.25*total_cost
  r=0.04

  def binarySearch():	     
    for n in range (0, 10000):
      middle = (ps1c().end - ps1c().start)/2
    if(ps1c().getMonths(start/10000)==36):
      return ps1c().start/10000
    elif(ps1c().getMonths(middle/10000)>36):
      ps1c().end = ps1c().middle-1
    else:
      ps1c().start = ps1c().middle+1
    ps1c().steps+=1  
    return -1

  def getMonths(portion_saved):
    month = 0
    current_savings = 0.0
    while (current_savings<ps1c().portion_down_payment):
     monthly = ps1c().annual_salary/12
     current_savings += ((current_savings*ps1c().r)/12)
     current_savings += (portion_saved*monthly)
     month+=1;
     if(month%6==0):
       annual_salary+=(ps1c().annual_salary*ps1c().semi_annual_raise)
    return month;

  num = binarySearch
  if(num!=-1):
    print('Best savings rate:', binarySearch())
    print('Steps in bisection search:', steps)
  else:
    print('It is not possible to pay the down payment in three years.')



