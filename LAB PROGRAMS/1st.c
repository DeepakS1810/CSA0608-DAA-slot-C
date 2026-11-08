#include <stdio.h>
#include <string.h>

int main() {
    char *words[] = {"abc", "car", "ada", "racecar", "cool"};
    int n = 5;

    for (int i = 0; i < n; i++) {
        int left = 0;
        int right = strlen(words[i]) - 1;
        int palindrome = 1;

        while (left < right) {
            if (words[i][left] != words[i][right]) {
                palindrome = 0;
                break;
            }
            left++;
            right--;
        }

        if (palindrome) {
            printf("%s", words[i]);
            return 0;
        }
    }

    printf("");
    return 0;
}