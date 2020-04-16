#include <stdio.h>
#include <stdlib.h>

char **swap_rows(int a, int b, int N, int M, char **board) {
    return board;
}

int main() {
    char board[8][8];
    char **board_p = malloc(sizeof(char)*8*8);
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            board[i][j] = !(i^j);
            board_p[i][j] = !(i^j);
            printf("(%d,%d): %d\n", i, j, board[i][j]);
            printf("(%d,%d): %d\n", i, j, board_p[i][j]);
        }
    }
}
