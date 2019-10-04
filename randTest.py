from random import *

countcount = 0
countsum = 0
for i in range(100000):
    digits = [0,0,0,0,0,0,0,0,0,0]
    count = 0
    done = 'nope'
    while done == 'nope':
        count += 1
#        print('Count:', count)
        int = randint(0,9)
#        print('int:', int)
        digits[int] = 1
        sum = 0
        for i in range(10):
            sum += digits[i]
        if sum == 10:
            done = 'yep'
    countcount += 1
    countsum += count
#    print('countcount =', countcount, 'countsum =', countsum)

avgcount = countsum/countcount

print('Average counts to complete:', avgcount)
