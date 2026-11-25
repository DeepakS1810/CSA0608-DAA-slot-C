#include <stdio.h>
#include <string.h>
int main(void) {
    char s[100];
    if (scanf("%99s", s) != 1) return 1;
    int n = (int)strlen(s), printed = 0;
    for (int i = 0; i < n;) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        if (j - i >= 3) { printf("%s[%d,%d]", printed++ ? " " : "", i, j - 1); }
        i = j;
    }
    putchar('\n');
    return 0;
}
