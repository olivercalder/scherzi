def count_string(string):
    if string:
        return 1 + count_string(string[1:])
    else:
        return 0

lambda_count = lambda string: 1 + lambda_count(string[1:]) if string else 0

print(count_string('hello'))
print(lambda_count('hello'))
print((lambda string: 1 + lambda_count(string[1:]) if string else 0)('hello'))
