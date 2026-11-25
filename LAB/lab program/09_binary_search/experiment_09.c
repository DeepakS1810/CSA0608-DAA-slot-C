#include <stdio.h>
int main(void) {
    int n, target;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    scanf("%d", &target);
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == target) { puts("Found"); return 0; }
        if (a[mid] < target) low = mid + 1; else high = mid - 1;
    }
    puts("Not Found");
    return 0;
}
