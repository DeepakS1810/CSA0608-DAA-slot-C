# Complexity and Experimental Notes

## Q1 Max-Min
For n a power of two with pairwise base cases: C(n)=2C(n/2)+2n/2? At each combine, compare the two minima and the two maxima (2 comparisons); base pairs use 1 comparison. This gives C(n)=3n/2−2 for even n under the standard paired tournament strategy. The recursive implementation in max_min.cpp combines two halves and uses two comparisons per internal node; its exact count depends on the base case and split convention. Independent scans use 2n−2 comparisons.

## Binary Search
Worst-case comparison growth is logarithmic. Successful and unsuccessful outcomes differ by target position and the exact comparison counter convention (the program separately counts equality and ordering tests).

## Q2
Merge Sort: T(n)=2T(n/2)+Θ(n)=Θ(n log n), predictable recursion depth Θ(log n).
Last-element Lomuto Quick Sort: balanced T(n)=2T(n/2)+Θ(n)=Θ(n log n); worst T(n)=T(n−1)+Θ(n)=Θ(n²). Sorted input with last-element pivot is a deliberately severe case.

## Q3
Standard digit multiplication: Θ(n²). Karatsuba: T(n)=3T(n/2)+Θ(n)=Θ(n^log₂3), log₂3≈1.585. String-based implementation has nontrivial addition/subtraction overhead; crossover depends on implementation and machine.

## Q4
Conventional matrix multiplication: Θ(n³). Strassen: T(n)=7T(n/2)+Θ(n²)=Θ(n^log₂7), exponent ≈2.807. Padding and additions increase constants and memory traffic.

## Q5
Brute force: Θ(n²) pair distances. D&C: T(n)=2T(n/2)+Θ(n)=Θ(n log n), provided points are presorted and the y-order is maintained through recursion. Strip packing geometry bounds comparisons per point by a constant.

## Q6
Median of Medians with groups of five: T(n)≤T(⌈n/5⌉)+T(7n/10+O(1))+Θ(n)=Θ(n). QuickSelect is expected Θ(n) with randomized pivots but worst Θ(n²).
Meet-in-the-Middle subset sum: O(2^(n/2) log 2^(n/2)) time using sorting/binary search and O(2^(n/2)) memory, versus Θ(2^n) exhaustive enumeration.

## Experimental integrity
Only benchmark figures in sorting_benchmark.csv and sorting_benchmark.png are measured by the included local C++17 benchmark harness. They are environment-specific, median of five runs, and not universal. Other sections report theoretical operation counts and deterministic sample outputs; no timing is claimed where no timed harness was run. Capture genuine screenshots locally; placeholder folders intentionally contain no fabricated screenshots.
