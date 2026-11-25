#include <stdio.h>
int main(void) {
    int n, k, count = 0;
    if (scanf("%d%d", &n, &k) != 2 || n < 1 || k == 0) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] == a[j] && ((long long)i * j) % k == 0) count++;
    printf("%d\n", count);
    return 0;
}
