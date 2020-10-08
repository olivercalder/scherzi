import itertools

perms = itertools.permutations(range(5))

def order_2(perm):
    good = True
    for i in range(5):
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
    total += 1
    if order_2(perm):
        count += 1
print(count)
