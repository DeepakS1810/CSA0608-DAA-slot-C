## TASK 9 – Record Experimental Performance (3 Marks)

**Method.** The records are the sorted registration numbers 0 to n−1 for n = 1,000; 10,000; 100,000 and 1,000,000. The Linear Search target is the last record (worst successful case) and is timed as the mean of repeated calls. Binary and hash lookups are averaged over 1,000 random keys. The hash table is built once and its build time is recorded separately. Times use time.perf_counter(). The program is Task_9_Experimental_Performance/run_experiments.py and its output is in Figure 9.2.

**Environment.** Python 3.12.3 on Linux (x86-64), Intel Xeon processor at 2.10 GHz, 1 virtual CPU, 4 GB RAM (cloud virtual machine). Results depend on the machine, so they are reported with their context.

| n | Linear: comparisons (worst) | Linear: time (ms) | Binary: comparisons (average) | Binary: time (ms per search) | Hash: build (ms) | Hash: time (ms per lookup) |
|---|---|---|---|---|---|---|
| 1,000 | 1,000 | 0.0224 | 8.99 | 0.00088 | 0.064 | 0.000051 |
| 10,000 | 10,000 | 0.2369 | 12.39 | 0.00136 | 0.717 | 0.000055 |
| 100,000 | 100,000 | 2.6649 | 15.65 | 0.00258 | 14.363 | 0.000108 |
| 1,000,000 | 1,000,000 | 24.4670 | 18.99 | 0.00332 | 101.897 | 0.000124 |

*Table 9.1 – Measured results (Task_9 run, Report/Tables_and_Graphs/experimental_results.csv)*

For reference, Table 9.2 gives the illustrative measurements supplied in the assignment text. They have the same trends as the measured values in Table 9.1 (Linear Search is roughly linear in n, Binary Search is very small, and Hash Lookup is fastest). The measured values are used for all analysis in this report.

| n | Linear (ms) | Recursive Binary (ms per search) | Hash (ms per lookup) |
|---|---|---|---|
| 1,000 | 0.032 | 0.001318 | 0.000106 |
| 10,000 | 0.496 | 0.002072 | 0.000055 |
| 100,000 | 3.557 | 0.002664 | 0.000059 |
| 1,000,000 | 40.813 | 0.002758 | 0.000105 |

*Table 9.2 – Illustrative measurements supplied in the assignment text*

![Figure 9.1 – Operation counts (left) and measured time per search (right); both axes logarithmic](Report/Tables_and_Graphs/performance_graphs.png)

*Figure 9.1 – Operation counts (left) and measured time per search (right); both axes logarithmic*

![Figure 9.2 – Execution output of run_experiments.py](Report/Output_Screenshots/Figure_O2_experiment_output.png)

*Figure 9.2 – Execution output of run_experiments.py*

| n | Linear (ms) | Binary (ms per search) | Hash (ms per lookup) | Binary average comparisons |
|---|---|---|---|---|
| 1,000 | 0.0251 ± 0.0026 | 0.001033 ± 0.000244 | 0.000065 ± 0.000017 | 8.95 |
| 10,000 | 0.2843 ± 0.0433 | 0.001404 ± 0.000032 | 0.000075 ± 0.000014 | 12.27 |
| 100,000 | 2.3292 ± 0.2128 | 0.001846 ± 0.000186 | 0.000081 ± 0.000006 | 15.74 |
| 1,000,000 | 20.1747 ± 0.3880 | 0.002598 ± 0.000150 | 0.000104 ± 0.000001 | 18.93 |

*Table 9.3 – Mean ± standard deviation over 5 independent trials (repeated_trials.csv)*

Table 9.3 repeats the timing five times for every size. The first run (Table 9.1) and the trial means differ by up to about 20 % for Linear Search, because the cloud machine's speed varies from one run to the next. For this reason the analysis in this report relies on operation counts and on orders of magnitude, not on any single timing. The standard deviations are small compared with the differences between methods.

![Figure 9.3 – Mean time per search with ±1 standard deviation over 5 trials](Report/Tables_and_Graphs/repeated_trials_errorbars.png)

*Figure 9.3 – Mean time per search with ±1 standard deviation over 5 trials*

**Interpretation.** Linear Search time rises by about a factor of 1,000 when n grows by a factor of 1,000, as expected for a Θ(n) method. Binary Search time rises only from 0.0009 ms to 0.0033 ms. Hash lookup stays between 0.00005 ms and 0.00012 ms, and the one-off hash build (about 102 ms at a million records) is the price of that speed.
