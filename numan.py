def f(x):
    return 3 * (x**3) - 24

a = 0
b = 3

mid = (a + b) / 2

while abs(f(mid)) > 0.0000000000000000000000000000001:
    if f(mid) > 0:
        b = mid
    else:
        a = mid
    mid = (a + b) / 2

print(mid)
