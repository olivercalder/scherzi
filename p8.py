import os
import sys

def check_range(a, b):
    solutions = set()
    for i in range(a, b):
        string = '{:010}'.format(i)
        array = []
        for j in range(10):
            array.append(int(string[j]))
        valid = True
        for k in range(10):
            if array[k] != array.count(k):
                valid = False
        if valid:
            solution = ''
            for h in range(10):
                solution = solution + str(array[h])
            solutions.add(solution)
    return solutions

if __name__ == '__main__':
    begin = 0
    end = 10000000000
    write = False
    if len(sys.argv) == 2:
        end = int(sys.argv[1])
    elif len(sys.argv) > 2:
        begin = int(sys.argv[1])
        end = int(sys.argv[2])
    if len(sys.argv) == 4:
        if sys.argv[3] == '-w':
            write = True
        else:
            print('Error: Unrecognized argument "{}"'.format(sys.argv[3]))
            quit()
    if len(sys.argv) == 1:
        print('Usage: python3 {} [[max] || [begin end]] [-w]'.format(sys.argv[0]))
        quit()
    solutions = check_range(begin, end)
    if write:
        with open('{}-{}.txt'.format(begin, end), 'w') as outfile:
            for solution in solutions:
                print(solution, file=outfile)
