## TASK 8 – Implement and Test the Algorithms (4 Marks)

The three strategies are implemented in Python 3 in Task_8_Implementation_Testing/Source_Code/search_algorithms.py. The file contains linear_search, binary_search (recursive, with low and high parameters), build_hash and hash_search. The complete source is listed in Appendix A and a screenshot is shown in Figure 8.1.

![Figure 8.1 – Screenshot of search_algorithms.py](Report/Source_Code_Screenshots/Figure_S1_search_algorithms.png)

*Figure 8.1 – Screenshot of search_algorithms.py*

**Testing procedure.** The file test_search.py runs eight deterministic tests and one randomised test. The deterministic tests cover the boundary cases (first, last and middle element, missing values, empty list, single element). The randomised test generates 200 sorted lists of random size and checks that all three methods agree on every key.

| # | Test | Result |
|---|---|---|
| 1 | Key at first position (0) | PASS |
| 2 | Key at last position (999) | PASS |
| 3 | Key in middle (500) | PASS |
| 4 | Missing key (−1) | PASS |
| 5 | Missing key (1000) | PASS |
| 6 | Empty list returns −1 | PASS |
| 7 | Single element found | PASS |
| 8 | Single element missing | PASS |
| 9 | 200 random sorted lists: all three methods agree | PASS |

*Table 8.1 – Correctness test cases and results*

![Figure 8.2 – Execution output of test_search.py (9 of 9 passed)](Report/Output_Screenshots/Figure_O1_correctness_tests.png)

*Figure 8.2 – Execution output of test_search.py (9 of 9 passed)*

| Method | Work performed for n = 1,000, key = 999 | Comparisons | Result |
|---|---|---|---|
| Linear Search | Examines A[0] to A[999] in turn | 999 | index 999 |
| Recursive Binary Search | Checks mid = 499, 749, 874, 937, 968, 984, 992, 996, 998, 999 | 10 | index 999 |
| Hash Lookup | One hash computation, one key check | 1 | index 999 |

*Table 8.2 – Trace of the three methods on the 1,000-record example (key 999)*

| Step | low | high | mid | A[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 9 | 4 | 4 | 7 > 4, so low = mid + 1 = 5 |
| 2 | 5 | 9 | 7 | 7 | equal: found at index 7 |

*Table 8.3 – Hand trace of binary search for n = 10, key = 7 (matches the program)*

The experiment program (Task 9) also cross-checks its own results: every binary and hash result is verified against the key, and the linear result against the known position, so a wrong answer would stop the run.
