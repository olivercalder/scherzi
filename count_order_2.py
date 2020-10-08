import itertools

order = 8

perms = itertools.permutations(range(order))

def order_2(perm):
    good = True
    for i in range(order):
        intermediate = perm[i]
        end = perm[intermediate]
        if i != end:
            good = False
    if good:
        print(perm)
        return True
    else:
        return False

count = 0
for perm in perms:
    if order_2(perm):
        count += 1
print(count)
