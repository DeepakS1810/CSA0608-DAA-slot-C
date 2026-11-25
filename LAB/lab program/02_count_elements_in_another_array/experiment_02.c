#include <stdio.h>
int main(void) {
    int n, m, first = 0, second = 0;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    scanf("%d", &m);
    if (m < 1) return 1;
    int b[m];
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) if (a[i] == b[j]) { first++; break; }
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) if (b[i] == a[j]) { second++; break; }
    }
    printf("%d %d\n", first, second);
    return 0;
}
