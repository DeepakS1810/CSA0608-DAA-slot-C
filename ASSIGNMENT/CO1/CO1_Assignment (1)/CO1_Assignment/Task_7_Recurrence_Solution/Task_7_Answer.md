## TASK 7 – Solve the Recurrence Relation (4 Marks)

### Iteration (backward substitution) for the running time

To keep the algebra clean, take n = 2^k so that floor(n/2) = n/2 exactly. Expanding the recurrence:

```
T(n)   = T(n/2)   + c
       = T(n/4)   + 2c
       = T(n/8)   + 3c
       = T(n/2^i) + i·c
```

The expansion stops when n / 2^i = 1, which gives i = log2 n. Substituting T(1) = d:

T(n) = T(1) + c·log2 n = d + c·log2 n = Θ(log n)

Each recursive call halves the input and performs constant work, so the depth and total work grow logarithmically.

### Exact solution of the comparison count

Since floor(n/2) is not always an integer, the exact count is obtained by counting the sizes in the sequence n, floor(n/2), floor(n/4), …, 1. This sequence has floor(log2 n) + 1 terms, and each term contributes one comparison. Therefore:

C(n) = floor(log2 n) + 1

Check against the recurrence for n = 2^k: C(2^k) = C(2^(k−1)) + 1 with C(1) = 1 gives C(2^k) = k + 1 = log2 n + 1, which agrees with the formula. For n = 1,000 the sequence 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1 has 10 terms, so C(1000) = 10.

| n | Predicted worst case floor(log2 n)+1 | Measured worst case | Predicted average log2 n − 1 | Measured average |
|---|---|---|---|---|
| 1,000 | 10 | 10 | 8.97 | 8.99 |
| 10,000 | 14 | 14 | 12.29 | 12.39 |
| 100,000 | 17 | 17 | 15.61 | 15.65 |
| 1,000,000 | 20 | 20 | 18.93 | 18.99 |

*Table 7.1 – Solution of the recurrence checked against the experiment (from Task 9)*
