#include <stdio.h>
long long rob_line(const int a[], int left, int right) {
    long long prev_two = 0, prev_one = 0;
    for (int i = left; i <= right; i++) {
        long long current = prev_two + a[i] > prev_one ? prev_two + a[i] : prev_one;
        prev_two = prev_one; prev_one = current;
    }
    return prev_one;
}
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    long long answer;
    if (n == 1) answer = a[0];
    else {
        long long without_last = rob_line(a, 0, n - 2);
        long long without_first = rob_line(a, 1, n - 1);
        answer = without_last > without_first ? without_last : without_first;
    }
    printf("%lld\n", answer);
    return 0;
}
