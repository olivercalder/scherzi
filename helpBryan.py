def test(result):
    if result == int(result):
        return True
    else:
        return False

def test_a(k):
    return test(k / (2*k - 15))

def test_b(k):
    return test(3 / (2*k - 15))

def test_c(k):
    return test(5 / (2*k - 15))

def test_d(k):
    return test(5 / (2*k - 15))

def get_k_values(tests):
    k_values = []
    for i in range(1000):
        solution = True
        if tests[0] == 1:
            solution = solution and test_a(i)
        if tests[1] == 1:
            solution = solution and test_b(i)
        if tests[2] == 1:
            solution = solution and test_c(i)
        if tests[3] == 1:
            solution = solution and test_d(i)
        if solution == True:
            k_values.append(i)
    return k_values

def main():
    k_values = []
    '''possible_values = {}
    for a in range(1, 10000):
        for b in range(-10000, 10000):
            value = b/a
            possible_values[value] = True
    for i in possible_values.keys():
        if i != 7.5:
            if test_a(i) and test_b(i) and test_c(i) and test_d(i):
               k_values.append(i)
    '''
    k_abc = get_k_values('1110')
    k_abd = get_k_values('1101')
    k_acd = get_k_values('1011')
    k_bcd = get_k_values('0111')

    print('k values with a, b, and c', k_abc)
    print('k values with a, b, and d', k_abd)
    print('k values with a, c, and d', k_acd)
    print('k values with b, c, and d', k_bcd)

main()
