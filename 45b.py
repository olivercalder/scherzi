import math

def choose(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def sum_of_squares(n):
    total = 0
    for k in range(n+1):
        total += (-1)**k * choose(n, k)**2
    return total

for i in range(20):
    print('{:3}: {}'.format(2*i, sum_of_squares(2*i)))
