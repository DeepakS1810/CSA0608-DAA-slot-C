#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    long long one = 1, two = 2;
    if (n <= 2) { printf("%d\n", n); return 0; }
    for (int i = 3; i <= n; i++) { long long next = one + two; one = two; two = next; }
    printf("%lld\n", two);
    return 0;
}
