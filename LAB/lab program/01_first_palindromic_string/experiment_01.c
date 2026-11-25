#include <stdio.h>
#include <string.h>
int main(void) {
    int n;
    char s[100][100];
    if (scanf("%d", &n) != 1 || n < 1 || n > 100) return 1;
    for (int i = 0; i < n; i++) scanf("%99s", s[i]);
    for (int i = 0; i < n; i++) {
        int left = 0, right = (int)strlen(s[i]) - 1, palindrome = 1;
        while (left < right) {
            if (s[i][left++] != s[i][right--]) { palindrome = 0; break; }
        }
        if (palindrome) { printf("%s\n", s[i]); return 0; }
    }
    puts("No palindrome");
    return 0;
}
