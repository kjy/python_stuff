balance = 4842   
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

Totalpaid=0.00             #After 1 year, what is your total payments and your remaining balance? 
for month in range(1,13):
    month_Interest_Rate = annualInterestRate/12.0
    min_month_payment = round((monthlyPaymentRate*balance),2)
    month_unpaid_balance = balance-min_month_payment
    interest = month_Interest_Rate*month_unpaid_balance
    balance = round((month_unpaid_balance + interest), 2)
    print ("Month: " + str(month))
    print ("Mininum monthly payment: " + str(min_month_payment))
    print ("Remaining balance: " + str(balance))
    Totalpaid = Totalpaid + min_month_payment
print ("Total paid: " + str(Totalpaid))
print ("Remaining balance: " + str(balance))


'''
test

balance = 5000    #say you have a credit card balance of $5K
annualInterestRate = 0.18  #you have an annual interest rate of 18%
monthlyPaymentRate = 0.02  #Your mininum payment is only $100 per month, which is 2%
Output:
    
Month: 1
Mininum monthly payment: 100.0
Remaining balance: 4973.5
Month: 2
Mininum monthly payment: 99.47
Remaining balance: 4947.14
Month: 3
Mininum monthly payment: 98.94
Remaining balance: 4920.92
Month: 4
Mininum monthly payment: 98.42
Remaining balance: 4894.84
Month: 5
Mininum monthly payment: 97.9
Remaining balance: 4868.89
Month: 6
Mininum monthly payment: 97.38
Remaining balance: 4843.08
Month: 7
Mininum monthly payment: 96.86
Remaining balance: 4817.41
Month: 8
Mininum monthly payment: 96.35
Remaining balance: 4791.88
Month: 9
Mininum monthly payment: 95.84
Remaining balance: 4766.48
Month: 10
Mininum monthly payment: 95.33
Remaining balance: 4741.22
Month: 11
Mininum monthly payment: 94.82
Remaining balance: 4716.1
Month: 12
Mininum monthly payment: 94.32
Remaining balance: 4691.11
Total paid: 1165.63
Remaining balance: 4691.11


balance = 4842   
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

Month: 1
Mininum monthly payment: 193.68
Remaining balance: 4725.79
Month: 2
Mininum monthly payment: 189.03
Remaining balance: 4612.37
Month: 3
Mininum monthly payment: 184.49
Remaining balance: 4501.68
Month: 4
Mininum monthly payment: 180.07
Remaining balance: 4393.64
Month: 5
Mininum monthly payment: 175.75
Remaining balance: 4288.19
Month: 6
Mininum monthly payment: 171.53
Remaining balance: 4185.27
Month: 7
Mininum monthly payment: 167.41
Remaining balance: 4084.82
Month: 8
Mininum monthly payment: 163.39
Remaining balance: 3986.79
Month: 9
Mininum monthly payment: 159.47
Remaining balance: 3891.11
Month: 10
Mininum monthly payment: 155.64
Remaining balance: 3797.73
Month: 11
Mininum monthly payment: 151.91
Remaining balance: 3706.58
Month: 12
Mininum monthly payment: 148.26
Remaining balance: 3617.63
Total paid: 2040.63
Remaining balance: 3617.63
'''
