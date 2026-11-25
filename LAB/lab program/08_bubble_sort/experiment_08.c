#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int pass = 0; pass < n - 1; pass++)
        for (int j = 0; j < n - pass - 1; j++)
            if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; }
    for (int i = 0; i < n; i++) printf("%s%d", i ? " " : "", a[i]);
    putchar('\n');
    return 0;
}
