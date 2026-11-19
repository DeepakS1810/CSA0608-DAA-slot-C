## TASK 10 – Compare Theory with Experimental Behaviour (4 Marks)

| Quantity | Theoretical prediction | Observed | Agreement |
|---|---|---|---|
| Linear worst-case comparisons | n | 1,000 to 1,000,000 (exact) | Exact |
| Linear time ratio, 1M vs 1k | 1,000 (linear) | 1,094 | Close (≈ 9% above) |
| Binary worst-case comparisons | floor(log2 n) + 1 = 10, 14, 17, 20 | 10, 14, 17, 20 | Exact |
| Binary average comparisons | log2 n − 1 = 8.97, 12.29, 15.61, 18.93 | 8.99, 12.39, 15.65, 18.99 | Within 0.1 comparison |
| Binary time ratio, 1M vs 1k | ≈ 2.0 (log n ratio) | 3.76 | Not matched; see text |
| Hash lookup probes | Θ(1), about 1 | 1 key access per query | Consistent |
| Hash lookup time, 1k to 1M | Nearly constant | 0.051 to 0.124 µs (≈ 2.4× for 1000× data) | Consistent |
| Hash build time, 1k to 1M | Θ(n): ×1,000 | 0.064 to 101.9 ms (×1,590) | Consistent (cache and resizing overheads) |
| Sort time, 1k to 1M | Θ(n log n): ×2,000 | 0.096 to 228.9 ms (×2,385) | Consistent (overheads at large n) |

*Table 10.1 – Predicted and observed behaviour*

**Where theory and measurement agree.** The operation counts match the mathematics exactly for Linear and Binary Search. Both the worst-case binary count and the linear count are exact integers, and the average binary count is within a tenth of a comparison of log2 n − 1. This is the strongest evidence in the report, because counts do not depend on the machine.

**Where theory and measurement differ.** The time ratio for Binary Search is 3.76 rather than the 2.0 predicted by log n. The reasons are: (i) each level of the search is a Python function call, which costs far more than the single comparison counted in the theory, so the fixed cost per search dominates at small n; (ii) at large n the array of a million integers and the dictionary are larger than the CPU cache, so each access at deeper levels can miss the cache; (iii) the timer resolution and system noise are significant for measurements of a few microseconds. These effects change the constant factor, not the growth class: the times still grow far more slowly than n.

| Ratio, 1,000,000 vs 1,000 records | Theory | First run | Mean of 5 trials |
|---|---|---|---|
| Linear time | 1,000 | 1,094 | 803 |
| Binary time | about 2.0 (log n) | 3.76 | 2.52 |
| Hash lookup time | about 1 | 2.43 | 1.60 |

*Table 10.2 – Time ratios from the two independent measurements*

Linear Search is between about 800 and 1,100 times slower at a million records, against a prediction of 1,000. Binary Search is slower than log n predicts, and its ratio varies most between runs, because its per-search time is only a few microseconds and is affected by timer resolution and call overhead. Hash lookup changes by a small factor at all sizes, as expected for a constant-time method.

**Conclusion.** The experiments support the growth-rate analysis: Linear Search is Θ(n), Binary Search is Θ(log n) and Hash lookup is Θ(1) on average. Exact times should not be generalised to other machines, so the system should be re-measured on its target hardware before deployment.
