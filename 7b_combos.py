import math
from itertools import combinations_with_replacement

x1 = 'x^4'
x2 = '2x^2'
x3 = '5x'

init_combs = combinations_with_replacement([x1, x2, x3], 10)
count = 0
final_combs = []
for comb in init_combs:
    print(comb)
    if 4 * comb.count(x1) + 2 * comb.count(x2) + comb.count(x3) == 30:
        final_combs.append(comb)
    count += 1

print()

total = 0
for comb in final_combs:
    print(comb)
    counts = [comb.count(x1), comb.count(x2), comb.count(x3)]
    print(counts)
    prod = math.factorial(10)
    for c in counts:
        prod //= math.factorial(c)

    for entry in comb:
        if entry[0].isdigit():
            prod *= int(entry[0])

    total += prod

print()

print('Coefficient of x^30 term:', total)
