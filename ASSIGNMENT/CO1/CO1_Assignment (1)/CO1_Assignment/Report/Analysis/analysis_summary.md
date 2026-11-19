# Analysis summary

**Task 10 – theory vs experiment.** Linear comparisons equal n exactly; binary worst-case comparisons equal floor(log2 n)+1 exactly
(10, 14, 17, 20); binary average comparisons are within 0.1 of log2 n − 1. Time ratios differ from the counts because of Python
call overhead and cache effects at large n, but they keep the same growth classes.

**Task 12 – work per hour at 1,000,000 records and 50,000 searches.**
- Linear Search, worst-case keys: 20.4 minutes (about 34 % of one core); average keys: about 10.2 minutes.
- Binary Search, sorted once: 0.39 s in total (229 ms sort + 166 ms queries).
- Hash table, built once: 0.11 s in total (102 ms build + 6.2 ms queries).

**Break-even.** The hash table repays its build against linear search after about 4 searches, and against binary search on
pre-sorted data after about 31,900 searches.
