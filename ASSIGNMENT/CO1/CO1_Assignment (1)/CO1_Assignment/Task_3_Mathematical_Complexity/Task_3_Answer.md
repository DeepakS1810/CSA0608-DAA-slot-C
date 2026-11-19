## TASK 3 – Derive the Time-Complexity Function Mathematically (6 Marks)

Let n be the number of records and let C(n) be the number of basic operations. A general running-time model is T(n) = a·C(n) + b, where a is the cost of one basic operation and b is fixed overhead.

### Linear Search

If the target is at position k (1-based), the loop performs k comparisons, so C(n) = k. If the target is absent, every record is compared, so C(n) = n. Averaged over all n equally likely successful positions:

C_avg(n) = (1/n) · (1 + 2 + … + n) = (1/n) · n(n+1)/2 = (n + 1) / 2

Therefore T(n) = a(n + 1)/2 + b = Θ(n). No preprocessing is required.

### Recursive Binary Search

Each call performs one comparison, then recurses on at most floor(n/2) records. Let C(n) be the worst-case number of comparisons for n records. Then:

C(n) = C(floor(n/2)) + 1 for n ≥ 2,    C(1) = 1,    C(0) = 0

Unrolling the recursion: after j calls the remaining interval has at most n / 2^j records. The interval contains one record when n / 2^j ≤ 1, i.e. j = floor(log2 n). Counting the comparisons made on the way down (one per call), the worst case is C(n) = floor(log2 n) + 1 = Θ(log n).

| Call j | Interval size n_j | Comparisons made so far |
|---|---|---|
| 0 | 1,000 | 1 |
| 1 | 500 | 2 |
| 2 | 250 | 3 |
| 3 | 125 | 4 |
| 4 | 62 | 5 |
| 5 | 31 | 6 |
| 6 | 15 | 7 |
| 7 | 7 | 8 |
| 8 | 3 | 9 |
| 9 | 1 | 10 |

*Table 3.1 – Unrolling the binary-search recurrence for n = 1,000: the sizes halve until one record is left*

The sequence has 10 terms, so the worst case is 10 comparisons, which equals floor(log2 1000) + 1.

If the data is not already sorted, sorting adds Θ(n log n). The total cost of one preparation plus one search is therefore Θ(n log n) + Θ(log n) = Θ(n log n). For repeated searches on mostly static data the sort is amortised over many queries.

### Hash-Table Lookup

Building the table performs n insertions. Each insertion takes expected constant time, so T_build(n) = c1·n + c2 = Θ(n). With chaining, the load factor α = n / m (n keys, m buckets) gives an expected number of probes of 1 + α/2 for a successful lookup and 1 + α for an unsuccessful one. Keeping α below a fixed constant (the table is resized when it grows) gives expected T_lookup(n) = Θ(1). For q lookups after construction, the expected total cost is Θ(n + q).

In the worst case, all keys fall into one bucket and a lookup examines n entries, giving O(n) per lookup and O(qn) for q lookups.
