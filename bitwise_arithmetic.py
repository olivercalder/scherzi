def bitwise_multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out += a
        a = a << 1
        b = b >> 1
    return out
