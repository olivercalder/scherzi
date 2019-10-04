import math
import sys

def main():
    if len(sys.argv) > 1:
        s = sys.argv[1]
    else:
        s = 4
    if len(sys.argv) > 2:
        x_max = sys.argv[2]
    else:
        x_max = 10
    for x in range(x_max + 1):
        t = math.sqrt(x**2 + s**2)
        print('( t = {0:0.4f} , x = {1:0.4f} )'.format(t, x))

main()
