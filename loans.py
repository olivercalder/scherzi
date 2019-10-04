principal = 2500
rate = 0.0505
daily_rate = rate / 365
increase = 1000
balance = 0
paid = 0

monthly_payment = 50
yearly_payment = 2500
continue_yearly_payment = False

for y in range(4):
    balance += principal + (increase * y)
    for d in range(365):
        balance *= 1 + daily_rate
    paid += yearly_payment
    balance -= yearly_payment

print('Amount paid during college: {}'.format(paid))
print('Total to pay: {}'.format(balance))

i = 0
while balance > 0:
    balance *= 1 + daily_rate
    if i % 30 == 0:
        paid += min(monthly_payment, balance)
        balance -= min(monthly_payment, balance)
    if continue_yearly_payment and i % 365 == 0:
        paid += min(yearly_payment, balance)
        balance -= min(yearly_payment, balance)
    i += 1

print('Days to pay off loan: {}'.format(i))
print('Total amount paid: {}'.format(paid))
