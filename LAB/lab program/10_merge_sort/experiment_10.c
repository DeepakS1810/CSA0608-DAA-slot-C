#include <stdio.h>
#include <stdlib.h>
void merge(int a[], int temp[], int left, int mid, int right) {
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right) temp[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    while (i <= mid) temp[k++] = a[i++];
    while (j <= right) temp[k++] = a[j++];
    for (i = left; i <= right; i++) a[i] = temp[i];
}
void merge_sort(int a[], int temp[], int left, int right) {
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    merge_sort(a, temp, left, mid);
    merge_sort(a, temp, mid + 1, right);
    merge(a, temp, left, mid, right);
}
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int *a = malloc((size_t)n * sizeof *a), *temp = malloc((size_t)n * sizeof *temp);
    if (!a || !temp) { free(a); free(temp); return 1; }
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    merge_sort(a, temp, 0, n - 1);
    for (int i = 0; i < n; i++) printf("%s%d", i ? " " : "", a[i]);
    putchar('\n'); free(a); free(temp);
    return 0;
}
