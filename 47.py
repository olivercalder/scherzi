def a(n):
#    print('n =', n)
    if n < 2:
        return 1
    rax = 0
    for k in range(1, n+1):
#        print('calling a({}) * a({})'.format(k-1, n-k))
        rax += a(k-1) * a(n-k)
    return rax

for i in range(2, 16):
    print('{:3}: {}'.format(i, a(i)))
