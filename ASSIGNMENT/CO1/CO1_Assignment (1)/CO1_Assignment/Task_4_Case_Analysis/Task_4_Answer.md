## TASK 4 – Best, Average and Worst Cases (4 Marks)

| Algorithm | Best case | Average case | Worst case |
|---|---|---|---|
| Linear Search | Target is first: 1 comparison, Θ(1) | Successful search, uniform target: (n+1)/2 comparisons, Θ(n) | Target last or absent: n comparisons, Θ(n) |
| Recursive Binary Search | Target is the middle element: 1 comparison, Θ(1) | Successful search: about log2 n − 1 comparisons, Θ(log n) | Target absent, or found at the deepest level: floor(log2 n) + 1 comparisons, Θ(log n) |
| Hash Lookup | Key in its first slot: 1 probe, Θ(1) | Good distribution: expected Θ(1) | Heavy collisions, all keys in one bucket: Θ(n) |

*Table 4.1 – Best, average and worst cases*

**Linear Search.** The number of comparisons depends only on the position of the target. For n = 1,000 the best case is 1 comparison, the average is 500.5 and the worst is 1,000.

**Binary Search.** Every comparison removes about half of the remaining candidates, so the result depends only logarithmically on n. For a successful search the average is about log2 n − 1 (the number of comparisons is governed by the depth of the implicit binary tree of midpoints, whose average depth is one less than its maximum). For n = 1,000 the average is about 9 and the worst case is 10.

**Hash Lookup.** The hash function sends the key to a small bucket, so the expected number of checks is a small constant. Only when many keys collide does the cost approach the linear case.

The average and worst case of Hash Lookup are stated under the assumption of simple uniform hashing. The registration numbers are not chosen by an adversary, so this assumption is reasonable for the system.
