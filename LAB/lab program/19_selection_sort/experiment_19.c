#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n - 1; i++) {
        int minimum = i;
        for (int j = i + 1; j < n; j++) if (a[j] < a[minimum]) minimum = j;
        int t = a[i]; a[i] = a[minimum]; a[minimum] = t;
    }
    for (int i = 0; i < n; i++) printf("%s%d", i ? " " : "", a[i]);
    putchar('\n');
    return 0;
}
