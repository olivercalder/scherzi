def add_link(path, n):
    if len(path) == 2*n:
        return [path]
    new_paths = []
    if path.count('u') < n:
        u_path = path.copy()
        u_path.append('u')
        new_paths += add_link(u_path, n)
    if path.count('r') < n:
        r_path = path.copy()
        r_path.append('r')
        new_paths += add_link(r_path, n)
    return new_paths

def count_above(path):
    total = 0
    for i in range(len(path)):
        link = path[i]
        if link == 'u' and path[:i].count('u') >= (i+1)//2:
            total += 1
    return total

def flip_path(path, u_num):
    i = 0
    count = 0
    while count < u_num:
        if path[i] == 'u':
            count += 1
        i += 1

path = []
n3_paths = add_link(path, 3)
print(len(n3_paths))
for p in n3_paths:
    print(''.join(p))
    print(count_above(p))
