import sys

def main():
    if len(sys.argv) == 1:
        print('This program calculates the coordinates of a simplex in n dimensions.')
        N = input('Input a positive integer for the dimension of the simplex: ')
        L = input('Input a number for the length of the edges: ')
    elif len(sys.argv) == 2:
        N = sys.argv[1]
        L = 1.0
    else:
        N = sys.argv[1]
        L = sys.argv[2]
    done_N = False
    while not done_N:
        try:
            N = int(N)
        except:
            pass
        if type(N) == type(1):
            if N >= 1:
                done_N = True
        else:
            print('\nThe number of dimensions must be a positive integer.')
            N = input('Input a positive integer for the dimension of the simplex: ')
    done_L = False
    while not done_L:
        try:
            L = float(L)
        except:
            pass
        if type(L) == type(1.0):
            if L > 0:
                done_L = True
        else:
            print('\nThe length of the edges must be greater than 0.')
            L = input('Input a number for the length of the edges: ')
    coordinates = []
    for i in range(N + 1):
        coordinates.append([])
        for j in range(N):
            coordinates[i].append(0)
    if N > 0:
        coordinates[1][0] = L
    for k in range(2, N + 1):
        coordinates[k] = coordinates[k-1].copy()
        coordinates[k][k-2] = coordinates[k][k-2] / 2
        coordinates[k][k-1] = (L**2 - (coordinates[k][k-2])**2)**(1/2)
    for point in coordinates:
        point_str = '{'
        for value in point:
            value_str = '{:9.4n}'.format(float(value))
            point_str = point_str + value_str + ', '
        point_str = point_str[:-2]
        point_str = point_str + '}'
        print(point_str)

main()
