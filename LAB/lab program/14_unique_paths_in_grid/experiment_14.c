#include <stdio.h>
int main(void) {
    int rows, cols;
    if (scanf("%d%d", &rows, &cols) != 2 || rows < 1 || cols < 1) return 1;
    long long paths[cols];
    for (int c = 0; c < cols; c++) paths[c] = 1;
    for (int r = 1; r < rows; r++)
        for (int c = 1; c < cols; c++) paths[c] += paths[c - 1];
    printf("%lld\n", paths[cols - 1]);
    return 0;
}
