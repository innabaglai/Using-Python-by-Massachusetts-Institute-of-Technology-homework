initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
monthlyPaymentLowerBound = balance / 12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
minPay = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2.0
month = 0
epsilon = 0.01

def calculate(month, balance, minPay, monthlyInterestRate):
    while month <12:
        unpaidBalance = balance - minPay
        balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
        month += 1
    return balance   
while abs(balance) >= epsilon:
    balance = initBalance
    month = 0
    balance = calculate(month, balance, minPay, monthlyInterestRate)
    if balance > 0:
        monthlyPaymentLowerBound = minPay
    else:
        monthlyPaymentUpperBound = minPay
    minPay = (monthlyPaymentUpperBound + monthlyPaymentLowerBound)/2.0
minPay = round(minPay,2)
print('Lowest Payment: ' + str(minPay))
