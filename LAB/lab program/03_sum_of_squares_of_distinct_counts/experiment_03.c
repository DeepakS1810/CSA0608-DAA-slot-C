#include <stdio.h>
int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1) return 1;
    int a[n];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    long long answer = 0;
    for (int start = 0; start < n; start++) {
        for (int end = start; end < n; end++) {
            int distinct = 0;
            for (int k = start; k <= end; k++) {
                int seen = 0;
                for (int j = start; j < k; j++) if (a[j] == a[k]) { seen = 1; break; }
                if (!seen) distinct++;
            }
            answer += (long long)distinct * distinct;
        }
    }
    printf("%lld\n", answer);
    return 0;
}
