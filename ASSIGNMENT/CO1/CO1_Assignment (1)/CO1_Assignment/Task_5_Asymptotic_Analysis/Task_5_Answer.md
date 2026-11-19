## TASK 5 – Asymptotic Analysis (3 Marks)

**Notation.** f(n) = O(g(n)) means f grows no faster than g (an upper bound). f(n) = Ω(g(n)) means f grows at least as fast as g (a lower bound). f(n) = Θ(g(n)) means f is bounded above and below by constant multiples of g, so g is the tight growth rate.

| Algorithm | Best case | Average case | Worst case | Preprocessing |
|---|---|---|---|---|
| Linear Search | Ω(1) (in fact Θ(1)) | Θ(n) | O(n) (tight: Θ(n)) | None |
| Recursive Binary Search | Ω(1) (Θ(1)) | Θ(log n) | O(log n) (tight: Θ(log n)) | Sort: Θ(n log n) |
| Hash Lookup | Ω(1) (Θ(1)) | Θ(1) expected | O(n) | Build: Θ(n) expected |

*Table 5.1 – Asymptotic classes of the three strategies*

Table 5.2 shows how the worst-case counts change over the range of record counts used in this assignment.

| n (records) | Linear worst comparisons | Binary worst comparisons | Hash probes (expected) |
|---|---|---|---|
| 1,000 | 1,000 | 10 | 1 |
| 10,000 | 10,000 | 14 | 1 |
| 100,000 | 100,000 | 17 | 1 |
| 1,000,000 | 1,000,000 | 20 | 1 |

*Table 5.2 – Operation counts as n grows 1,000-fold*

When n grows from 1,000 to 1,000,000, Linear Search performs 1,000 times more comparisons, Binary Search performs only 10 more (from 10 to 20), and Hash Lookup stays at about one probe. Binary Search is therefore Θ(log n), not Θ(n), and the hash lookup is constant on average.
