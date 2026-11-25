#include <stdio.h>
int main(void) {
    int rows, cols;
    if (scanf("%d%d", &rows, &cols) != 2 || rows < 1 || cols < 1) return 1;
    int a[rows][cols], next[rows][cols];
    for (int r = 0; r < rows; r++) for (int c = 0; c < cols; c++) scanf("%d", &a[r][c]);
    for (int r = 0; r < rows; r++) for (int c = 0; c < cols; c++) {
        int neighbors = 0;
        for (int dr = -1; dr <= 1; dr++) for (int dc = -1; dc <= 1; dc++) {
            int nr = r + dr, nc = c + dc;
            if ((dr || dc) && nr >= 0 && nr < rows && nc >= 0 && nc < cols)
                neighbors += a[nr][nc];
        }
        next[r][c] = a[r][c] ? (neighbors == 2 || neighbors == 3) : (neighbors == 3);
    }
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) printf("%s%d", c ? " " : "", next[r][c]);
        putchar('\n');
    }
    return 0;
}
