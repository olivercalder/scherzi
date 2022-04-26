def difference(number, n):
    row_mask = (1 << n) - 1
    rows = 0
    cols = 0
    for i in range(n):
        rows += (number >> (n * i)) & row_mask
        col = 0
        for j in range(n):
            col |= ((number >> (n * j + i)) & 1) << j
        cols += col
    return cols - rows

def print_matrix(number, n):
    matrix_format = '{' + f':0{n}b' + '}'
    row_mask = (1 << n) - 1
    for i in range(n):
        print(matrix_format.format((number >> (n * (n - i - 1))) & row_mask))

def find_max_d(n):
    limit = 1 << (n * n)
    best_d = 0
    best_numbers = []
    for i in range(limit):
        d = difference(i, n)
        if d > best_d:
            best_numbers = [i]
            best_d = d
        elif d == best_d:
            best_numbers.append(i)
    return best_d, best_numbers

def main():
    for n in range(2, 6):
        best_d, best_numbers = find_max_d(n)
        print(f'\n\nBest D for n={n}: {best_d}\n')
        '''
        for number in best_numbers:
            print_matrix(number, n)
            print()
        '''

if __name__ == '__main__':
    main()
    # print(find_max_d(4)[0])
