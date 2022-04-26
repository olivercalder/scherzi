#include <stdio.h>

long long difference(unsigned long long number, size_t n) {
    unsigned long long i, j, col, rows = 0, cols = 0, row_mask = (1 << n) - 1;
    for (i = 0; i < n; i++) {
        rows += (number >> (n * i)) & row_mask;
        col = 0;
        for (j = 0; j < n; j++) {
            col |= ((number >> (n * j + i)) & 1) << j;
        }
        cols += col;
    }
    return (long long) (cols - rows);
}

long long find_max_d(size_t n) {
    long long d, better_mask, best_d = ~0;
    unsigned long long i, limit = 1 << (n * n);
    for (i = 0; i < limit; i++) {
        d = difference(i, n);
        //better_mask = (best_d - d) >> 63;
        //best_d = (better_mask & d) | (~better_mask & best_d);
        if (d > best_d) best_d = d;
    }
    return best_d;
}

void main() {
    size_t n = 4;
    printf("%lld", find_max_d(n));
}
