#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int value, maximum;
    scanf("%d", &maximum);
    for (int i = 1; i < n; i++) {
        scanf("%d", &value);
        if (value > maximum) maximum = value;
    }
    printf("%d\n", maximum);
    return 0;
}
