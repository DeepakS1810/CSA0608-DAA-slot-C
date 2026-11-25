#include <stdio.h>
long long memo[10][10][20];
int rows, cols;
long long paths(int r, int c, int steps) {
    if (r < 0 || r >= rows || c < 0 || c >= cols) return 1;
    if (steps == 0) return 0;
    if (memo[r][c][steps] != -1) return memo[r][c][steps];
    return memo[r][c][steps] = paths(r + 1, c, steps - 1) + paths(r - 1, c, steps - 1)
        + paths(r, c + 1, steps - 1) + paths(r, c - 1, steps - 1);
}
int main(void) {
    int max_steps;
    if (scanf("%d%d%d", &rows, &cols, &max_steps) != 3 || rows < 1 || rows > 10
        || cols < 1 || cols > 10 || max_steps < 0 || max_steps > 19) return 1;
    for (int r = 0; r < 10; r++) for (int c = 0; c < 10; c++)
        for (int s = 0; s < 20; s++) memo[r][c][s] = -1;
    printf("%lld\n", paths(0, 0, max_steps));
    return 0;
}
