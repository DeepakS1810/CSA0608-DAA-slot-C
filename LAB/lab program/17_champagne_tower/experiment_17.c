#include <stdio.h>
int main(void) {
    double poured;
    int row, glass;
    if (scanf("%lf%d%d", &poured, &row, &glass) != 3 || row < 0 || row > 99
        || glass < 0 || glass > row) return 1;
    double amount[101][101] = {{0}};
    amount[0][0] = poured;
    for (int r = 0; r < row; r++) for (int c = 0; c <= r; c++) {
        double overflow = (amount[r][c] - 1.0) / 2.0;
        if (overflow > 0) { amount[r + 1][c] += overflow; amount[r + 1][c + 1] += overflow; }
    }
    double result = amount[row][glass];
    if (result > 1) result = 1;
    printf("%.2f\n", result);
    return 0;
}
