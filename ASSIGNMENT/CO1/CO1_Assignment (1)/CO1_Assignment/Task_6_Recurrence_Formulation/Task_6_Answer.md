## TASK 6 – Formulate the Recurrence Relation (3 Marks)

The recursive search is binary_search(A, key, 0, n−1). Each call performs constant work (computing mid and one comparison) and at most one recursive call on a subarray of size at most floor(n/2). The base cases are an empty interval (low > high) and a successful match.

**Running time** (constant c for work per call, d for the base case):

```
T(n) = T(floor(n/2)) + c    for n > 1
T(1)    = d
T(0)    = d0
```

**Comparison count** (the basic operation of Task 2, so c = 1 and d = 1):

```
C(n) = C(floor(n/2)) + 1   for n ≥ 2
C(1)    = 1
C(0)    = 0
```

The recurrence follows directly from the algorithm: a constant amount of work is performed, then at most half of the records remain to be searched.
