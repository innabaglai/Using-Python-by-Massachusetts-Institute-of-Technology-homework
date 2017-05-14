MinimumFixedMonthlyPayment = 10
new_balance = 0
def bal_funk(balance, annualInterestRate, MinimumFixedMonthlyPayment):
  for i in range(1,13):
    MonthlyInterestRate = annualInterestRate / 12.0
    MonthlyUnpaidBalance = balance - MinimumFixedMonthlyPayment
    balance = MonthlyUnpaidBalance + (MonthlyInterestRate * MonthlyUnpaidBalance)
  return balance
while new_balance >= 0:
  MinimumFixedMonthlyPayment += 10
  new_balance = bal_funk(balance, annualInterestRate, MinimumFixedMonthlyPayment) 
print('Lowest Payment: '+str(round(MinimumFixedMonthlyPayment)))

