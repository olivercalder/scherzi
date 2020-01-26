import sys
import math

def probability(n, k):
    total = 0.0
    for i in range(n-k+1):
        total += (-1)**i * 1/(math.factorial(i) * math.factorial(k))
    return total

def main():
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
        total = 0.0
        for k in range(0, n+1):
            total += probability(n, k)
        print('Sum of probabilities for all 0<=k<=n where n={}: {}'.format(n, total))
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        total = probability(n, k)
        print('Total for k={}, n={}: {}'.format(k, n, total))
    else:
        print('Usage: python3 {} n [k]'.format(sys.argv[0]))
        quit()

if __name__ == '__main__':
    main()
