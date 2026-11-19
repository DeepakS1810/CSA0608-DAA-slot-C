# CSA06 – Assignment 1 (CO1): Search Strategies for a Student Record System

Three search strategies are designed, analysed, implemented, tested and measured:
Iterative **Linear Search**, Recursive **Binary Search** and **Hash-Table Lookup**.

## Folder guide

| Folder | Contents |
|---|---|
| `Task_1_Algorithm_Design/` | Task 1 answer (`Task_1_Answer.md`): design and pseudocode of the three algorithms |
| `Task_2_Basic_Operation/` | Task 2 answer: basic operation of each algorithm |
| `Task_3_Mathematical_Complexity/` | Task 3 answer: derivation of time complexity |
| `Task_4_Case_Analysis/` | Task 4 answer: best, average and worst cases |
| `Task_5_Asymptotic_Analysis/` | Task 5 answer: Ω, Θ, O classes and growth table |
| `Task_6_Recurrence_Formulation/` | Task 6 answer: recurrence relations |
| `Task_7_Recurrence_Solution/` | Task 7 answer: iteration method and exact solution |
| `Task_8_Implementation_Testing/` | Task 8 answer and `Source_Code/` (`search_algorithms.py`, `test_search.py`) |
| `Task_9_Experimental_Performance/` | Task 9 answer and `run_experiments.py` (measurements and graphs) |
| `Task_10_Theory_vs_Experiment/` | Task 10 answer: predicted vs observed behaviour |
| `Task_11_Final_Recommendation/` | Task 11 answer: recommended design with justification |
| `Task_12_Design_Challenge/` | Task 12 answer: impact, evaluation, redesign and defence |
| `Report/` | Full report (`.docx`), screenshots, tables and graphs, documentation |

### Inside `Report/`
- `CO1_Assignment_1_Search_Strategies_Report.docx`: the complete report.
- `Source_Code_Screenshots/`: screenshots of the source files (`Figure_S1`–`S3`).
- `Output_Screenshots/`: screenshots of test and experiment output (`Figure_O1`, `Figure_O2`) and the plain-text outputs.
- `Tables_and_Graphs/`: `experimental_results.csv` (first run), `repeated_trials.csv` (5 trials with standard deviations), and the graphs `performance_graphs.png` and `repeated_trials_errorbars.png`.
- `Analysis/`: written analysis (Task 10 and Task 12 summaries).
- `Documentation/`: report generator (`content.py` is the single source of the text, `build_docx.js` builds the Word file, `build_markdown.py` writes the per-task answers).

## How to reproduce

Requires Python 3.9+ and matplotlib (for graphs). Run from this folder:

```bash
cd Task_8_Implementation_Testing/Source_Code && python test_search.py     # correctness tests (9 tests)
cd ../.. && python Task_9_Experimental_Performance/run_experiments.py      # timings and graphs
python Task_9_Experimental_Performance/repeat_trials.py                    # 5 repeated trials (mean and SD)
```

Operation counts (comparisons) are the primary evidence and are identical on every machine. Timings depend on the hardware;
the values in the report were measured on a 2.10 GHz Intel Xeon virtual CPU with Python 3.12.3.

## Key results

| n | Linear worst (comparisons) | Binary average (comparisons) | Hash (expected probes) |
|---|---|---|---|
| 1,000 | 1,000 | 8.99 | 1 |
| 10,000 | 10,000 | 12.39 | 1 |
| 100,000 | 100,000 | 15.65 | 1 |
| 1,000,000 | 1,000,000 | 18.99 | 1 |

**Recommendation:** a hash table keyed by registration number, built once and updated daily (Task 11).
