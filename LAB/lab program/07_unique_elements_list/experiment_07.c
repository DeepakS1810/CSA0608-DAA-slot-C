#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n], unique[n], size = 0;
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < size; j++) if (unique[j] == a[i]) { found = 1; break; }
        if (!found) unique[size++] = a[i];
    }
    for (int i = 0; i < size; i++) printf("%s%d", i ? " " : "", unique[i]);
    putchar('\n');
    return 0;
}
