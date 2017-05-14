total_paid = 0.00
month = 1
while(month <= 12):
    monthly_interest_rate = annualInterestRate / 12.0
    minimum_monthly_payment = monthlyPaymentRate * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    total_paid += minimum_monthly_payment
    month += 1
print('Remaining balance: '+str(round(balance,2)))

