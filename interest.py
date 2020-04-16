def calc_total(principle, y_int, payment, comp_first=True):
    total = 0.0
    while principle > 0:
        if comp_first:
            principle *= 1.0 + (y_int / 12)
        pay = min(principle, payment)
        total += pay
        principle -= pay
        if not comp_first:
            principle *= 1.0 + (y_int / 12)
    return total


balance = 360000
payment = 2400
interest = 0.0265

print()
print('Init Balance: ${:.2f}'.format(balance))
print('    Payments: ${:.2f}'.format(payment))
print('        Rate:  {}%'.format(interest))
print('       Total: ${:.2f}'.format(calc_total(balance, interest, payment, True) + 6513))
print('    Interest: ${:.2f}'.format(calc_total(balance, interest, payment, True) - balance))
print()
