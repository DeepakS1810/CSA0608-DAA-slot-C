"""Single source of truth for the report text. build_outputs.py turns this into content.json
(for the Word builder) and into the per-task Markdown answer files."""
import os, json, csv, sys
from PIL import Image
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
R = lambda *p: os.path.join(ROOT, *p)
B = []                       # blocks
def h1(x, task=None):
    if task is not None or x in ("Conclusion", "References", "Limitations and Threats to Validity") or x.startswith("Appendix"):
        pb()
    B.append({"t": "h1", "x": x, "task": task})
def h2(x, task=None): B.append({"t": "h2", "x": x, "task": task})
def h3(x, task=None): B.append({"t": "h3", "x": x, "task": task})
def p(x, task=None): B.append({"t": "p", "x": x, "task": task})
def bul(items, task=None): B.append({"t": "bul", "items": items, "task": task})
def code(x, task=None): B.append({"t": "code", "x": x, "task": task})
def table(head, rows, w, caption, task=None): B.append({"t": "table", "head": head, "rows": rows, "w": w, "caption": caption, "task": task})
def img(path, caption, task=None, w_in=6.0):
    im = Image.open(path); B.append({"t": "img", "src": path, "caption": caption, "task": task, "w_in": w_in, "px": im.size})
def pb(): B.append({"t": "pb"})

# ----------------------------------------------------------------- Cover
B.append({"t": "cover"})
pb()
h1("CONTENTS")
for line in ["Introduction", "Task 1 – Design the Algorithms", "Task 2 – Identify the Basic Operation",
             "Task 3 – Derive the Time-Complexity Function Mathematically", "Task 4 – Best, Average and Worst Cases",
             "Task 5 – Asymptotic Analysis", "Task 6 – Formulate the Recurrence Relation",
             "Task 7 – Solve the Recurrence Relation", "Task 8 – Implement and Test the Algorithms",
             "Task 9 – Record Experimental Performance", "Task 10 – Compare Theory with Experimental Behaviour",
             "Task 11 – Recommend and Defend the Final Design", "Task 12 – Design Challenge",
             "Conclusion", "References", "Appendix A – Source Code", "Appendix B – Raw Experimental Data"]:
    bul([line])
pb()

# ----------------------------------------------------------------- Introduction
h1("Introduction")
p("A large-scale student record system stores registration numbers and student details. The system must retrieve a record "
  "quickly when a registration number is entered. As the number of records grows, the choice of search strategy determines "
  "response time and scalability.")
p("This assignment studies three approaches: iterative Linear Search, Recursive Binary Search and Hash-Table Lookup. Each is "
  "designed, analysed mathematically, implemented in Python, tested for correctness and measured experimentally on 1,000 to "
  "1,000,000 records. The theoretical predictions are then compared with the measurements.")
p("**Assumptions.** Registration numbers are unique. Linear Search works on unsorted data. Binary Search requires sorted data. "
  "Hash-table lookup is expected to be constant-time when the hash function distributes keys well and the load factor is controlled.")
p("**Evidence.** Operation counts (key comparisons) are the primary evidence because they do not depend on the machine. Times are "
  "supporting evidence, measured on the environment described in Task 9. All numbers in this report come from the programs in "
  "the Task_8 and Task_9 folders; the raw data is in Report/Tables_and_Graphs.")

# ----------------------------------------------------------------- TASK 1
T = 1
h1("TASK 1 – Design the Algorithms (5 Marks)", T)
h2("1. Iterative Linear Search", T)
p("**Basic idea.** Inspect each registration number from the beginning until the key is found or the list ends. It needs no "
  "sorting, so it is the baseline for unsorted records.", T)
code("LINEAR-SEARCH(A, key)\n    for i = 0 to length(A) - 1\n        if A[i] == key\n            return i\n    return -1", T)
h2("2. Recursive Binary Search", T)
p("**Basic idea.** Search a sorted array by comparing the key with the middle element. If the key is smaller, search only the left "
  "half; if larger, only the right half. Each call discards about half of the remaining candidates. The records must be sorted "
  "beforehand; a comparison sort costs O(n log n).", T)
code("BINARY-SEARCH(A, key, low, high)\n    if low > high: return -1\n    mid = low + (high - low) // 2\n    if A[mid] == key: return mid\n    if key < A[mid]:\n        return BINARY-SEARCH(A, key, low, mid - 1)\n    return BINARY-SEARCH(A, key, mid + 1, high)", T)
p("The midpoint is computed as low + (high − low) // 2 rather than (low + high) // 2. The two are equal in mathematics, but the "
  "first form cannot overflow in fixed-width integer languages, which is good practice for an index calculation.", T)
h2("3. Hash-Table Lookup", T)
p("**Basic idea.** Store each registration number as a key in a hash table. A hash function maps the key to a slot or bucket. "
  "Building the table is preprocessing that takes expected O(n) time; a lookup takes expected O(1) time when collisions are controlled.", T)
code("BUILD-HASH(records)\n    create empty hash table H\n    for each record r in records:\n        H[r.registration_number] = r\n    return H\n\nHASH-SEARCH(H, key)\n    if key is in H: return H[key]\n    return NOT-FOUND", T)
p("Hash-table lookup differs from the two comparison-based methods. Its expected cost depends on the hash function and the load "
  "factor rather than on the number of comparisons with keys, and its worst case (all keys in one bucket) degrades to O(n).", T)
p("**Design summary.** Linear Search trades speed for simplicity and needs no preprocessing. Binary Search needs sorted data but "
  "uses very few comparisons. Hash lookup spends extra time and memory on an index, then answers each query in almost constant time.", T)

# ----------------------------------------------------------------- TASK 2
T = 2
h1("TASK 2 – Identify the Basic Operation (2 Marks)", T)
p("The basic operation is the operation that is executed most often and therefore determines the count of work. In all three "
  "algorithms it is the comparison of the search key with a stored registration number. Other steps (loop increments, computing "
  "mid, returning a value) take a fixed amount of time per iteration and do not change the order of growth.", T)
table(["Algorithm", "Basic operation", "Why this is the basic operation", "Count behaviour"],
      [["Linear Search", "Equality test A[i] == key", "Executed once for each record examined; it is the only work inside the loop", "One test per examined record: 1 to n"],
       ["Recursive Binary Search", "Comparison of key with A[mid]", "Executed once per recursive call; the call itself and the mid calculation are constant extra work", "One comparison per level; the interval halves each time"],
       ["Hash Lookup", "Hash calculation h(key) and key check in the selected slot", "Each lookup performs one hash calculation and at most a few key checks in its bucket", "Expected a constant number of checks; heavy collisions can force many"]],
      [0.18, 0.24, 0.36, 0.22], "Table 2.1 – Basic operations of the three strategies", T)
p("In the Python program (Task 8) the counts used for Linear and Binary Search are key comparisons, and the Hash lookup is one "
  "dictionary access, which Python performs with one hash computation and expected one key check.", T)

# ----------------------------------------------------------------- TASK 3
T = 3
h1("TASK 3 – Derive the Time-Complexity Function Mathematically (6 Marks)", T)
p("Let n be the number of records and let C(n) be the number of basic operations. A general running-time model is T(n) = a·C(n) + b, "
  "where a is the cost of one basic operation and b is fixed overhead.", T)
h2("Linear Search", T)
p("If the target is at position k (1-based), the loop performs k comparisons, so C(n) = k. If the target is absent, every record is "
  "compared, so C(n) = n. Averaged over all n equally likely successful positions:", T)
p("C_avg(n) = (1/n) · (1 + 2 + … + n) = (1/n) · n(n+1)/2 = (n + 1) / 2", T)
p("Therefore T(n) = a(n + 1)/2 + b = Θ(n). No preprocessing is required.", T)
h2("Recursive Binary Search", T)
p("Each call performs one comparison, then recurses on at most floor(n/2) records. Let C(n) be the worst-case number of comparisons "
  "for n records. Then:", T)
p("C(n) = C(floor(n/2)) + 1 for n ≥ 2,    C(1) = 1,    C(0) = 0", T)
p("Unrolling the recursion: after j calls the remaining interval has at most n / 2^j records. The interval contains one record when "
  "n / 2^j ≤ 1, i.e. j = floor(log2 n). Counting the comparisons made on the way down (one per call), the worst case is "
  "C(n) = floor(log2 n) + 1 = Θ(log n).", T)
_sizes = [1000]
while _sizes[-1] > 1:
    _sizes.append(_sizes[-1] // 2)
table(["Call j", "Interval size n_j", "Comparisons made so far"],
      [[str(j), f"{v:,}", str(j + 1)] for j, v in enumerate(_sizes)],
      [0.2, 0.4, 0.4], "Table 3.1 – Unrolling the binary-search recurrence for n = 1,000: the sizes halve until one record is left", T)
p("The sequence has 10 terms, so the worst case is 10 comparisons, which equals floor(log2 1000) + 1.", T)
p("If the data is not already sorted, sorting adds Θ(n log n). The total cost of one preparation plus one search is therefore "
  "Θ(n log n) + Θ(log n) = Θ(n log n). For repeated searches on mostly static data the sort is amortised over many queries.", T)
h2("Hash-Table Lookup", T)
p("Building the table performs n insertions. Each insertion takes expected constant time, so T_build(n) = c1·n + c2 = Θ(n). "
  "With chaining, the load factor α = n / m (n keys, m buckets) gives an expected number of probes of 1 + α/2 for a successful lookup "
  "and 1 + α for an unsuccessful one. Keeping α below a fixed constant (the table is resized when it grows) gives expected "
  "T_lookup(n) = Θ(1). For q lookups after construction, the expected total cost is Θ(n + q).", T)
p("In the worst case, all keys fall into one bucket and a lookup examines n entries, giving O(n) per lookup and O(qn) for q lookups.", T)

# ----------------------------------------------------------------- TASK 4
T = 4
h1("TASK 4 – Best, Average and Worst Cases (4 Marks)", T)
table(["Algorithm", "Best case", "Average case", "Worst case"],
      [["Linear Search", "Target is first: 1 comparison, Θ(1)", "Successful search, uniform target: (n+1)/2 comparisons, Θ(n)", "Target last or absent: n comparisons, Θ(n)"],
       ["Recursive Binary Search", "Target is the middle element: 1 comparison, Θ(1)", "Successful search: about log2 n − 1 comparisons, Θ(log n)", "Target absent, or found at the deepest level: floor(log2 n) + 1 comparisons, Θ(log n)"],
       ["Hash Lookup", "Key in its first slot: 1 probe, Θ(1)", "Good distribution: expected Θ(1)", "Heavy collisions, all keys in one bucket: Θ(n)"]],
      [0.2, 0.26, 0.28, 0.26], "Table 4.1 – Best, average and worst cases", T)
p("**Linear Search.** The number of comparisons depends only on the position of the target. For n = 1,000 the best case is 1 "
  "comparison, the average is 500.5 and the worst is 1,000.", T)
p("**Binary Search.** Every comparison removes about half of the remaining candidates, so the result depends only logarithmically on n. "
  "For a successful search the average is about log2 n − 1 (the number of comparisons is governed by the depth of the implicit "
  "binary tree of midpoints, whose average depth is one less than its maximum). For n = 1,000 the average is about 9 and the worst "
  "case is 10.", T)
p("**Hash Lookup.** The hash function sends the key to a small bucket, so the expected number of checks is a small constant. Only "
  "when many keys collide does the cost approach the linear case.", T)
p("The average and worst case of Hash Lookup are stated under the assumption of simple uniform hashing. The registration numbers "
  "are not chosen by an adversary, so this assumption is reasonable for the system.", T)

# ----------------------------------------------------------------- TASK 5
T = 5
h1("TASK 5 – Asymptotic Analysis (3 Marks)", T)
p("**Notation.** f(n) = O(g(n)) means f grows no faster than g (an upper bound). f(n) = Ω(g(n)) means f grows at least as fast as g "
  "(a lower bound). f(n) = Θ(g(n)) means f is bounded above and below by constant multiples of g, so g is the tight growth rate.", T)
table(["Algorithm", "Best case", "Average case", "Worst case", "Preprocessing"],
      [["Linear Search", "Ω(1) (in fact Θ(1))", "Θ(n)", "O(n) (tight: Θ(n))", "None"],
       ["Recursive Binary Search", "Ω(1) (Θ(1))", "Θ(log n)", "O(log n) (tight: Θ(log n))", "Sort: Θ(n log n)"],
       ["Hash Lookup", "Ω(1) (Θ(1))", "Θ(1) expected", "O(n)", "Build: Θ(n) expected"]],
      [0.22, 0.2, 0.18, 0.22, 0.18], "Table 5.1 – Asymptotic classes of the three strategies", T)
p("Table 5.2 shows how the worst-case counts change over the range of record counts used in this assignment.", T)
table(["n (records)", "Linear worst comparisons", "Binary worst comparisons", "Hash probes (expected)"],
      [["1,000", "1,000", "10", "1"], ["10,000", "10,000", "14", "1"], ["100,000", "100,000", "17", "1"], ["1,000,000", "1,000,000", "20", "1"]],
      [0.25, 0.25, 0.25, 0.25], "Table 5.2 – Operation counts as n grows 1,000-fold", T)
p("When n grows from 1,000 to 1,000,000, Linear Search performs 1,000 times more comparisons, Binary Search performs only 10 more "
  "(from 10 to 20), and Hash Lookup stays at about one probe. Binary Search is therefore Θ(log n), not Θ(n), and the hash lookup "
  "is constant on average.", T)

# ----------------------------------------------------------------- TASK 6
T = 6
h1("TASK 6 – Formulate the Recurrence Relation (3 Marks)", T)
p("The recursive search is binary_search(A, key, 0, n−1). Each call performs constant work (computing mid and one comparison) "
  "and at most one recursive call on a subarray of size at most floor(n/2). The base cases are an empty interval (low > high) "
  "and a successful match.", T)
p("**Running time** (constant c for work per call, d for the base case):", T)
code("T(n) = T(floor(n/2)) + c    for n > 1\nT(1)    = d\nT(0)    = d0", T)
p("**Comparison count** (the basic operation of Task 2, so c = 1 and d = 1):", T)
code("C(n) = C(floor(n/2)) + 1   for n ≥ 2\nC(1)    = 1\nC(0)    = 0", T)
p("The recurrence follows directly from the algorithm: a constant amount of work is performed, then at most half of the records "
  "remain to be searched.", T)

# ----------------------------------------------------------------- TASK 7
T = 7
h1("TASK 7 – Solve the Recurrence Relation (4 Marks)", T)
h2("Iteration (backward substitution) for the running time", T)
p("To keep the algebra clean, take n = 2^k so that floor(n/2) = n/2 exactly. Expanding the recurrence:", T)
code("T(n)   = T(n/2)   + c\n       = T(n/4)   + 2c\n       = T(n/8)   + 3c\n       = T(n/2^i) + i·c", T)
p("The expansion stops when n / 2^i = 1, which gives i = log2 n. Substituting T(1) = d:", T)
p("T(n) = T(1) + c·log2 n = d + c·log2 n = Θ(log n)", T)
p("Each recursive call halves the input and performs constant work, so the depth and total work grow logarithmically.", T)
h2("Exact solution of the comparison count", T)
p("Since floor(n/2) is not always an integer, the exact count is obtained by counting the sizes in the sequence n, floor(n/2), "
  "floor(n/4), …, 1. This sequence has floor(log2 n) + 1 terms, and each term contributes one comparison. Therefore:", T)
p("C(n) = floor(log2 n) + 1", T)
p("Check against the recurrence for n = 2^k: C(2^k) = C(2^(k−1)) + 1 with C(1) = 1 gives C(2^k) = k + 1 = log2 n + 1, which "
  "agrees with the formula. For n = 1,000 the sequence 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1 has 10 terms, so C(1000) = 10.", T)
table(["n", "Predicted worst case floor(log2 n)+1", "Measured worst case", "Predicted average log2 n − 1", "Measured average"],
      [["1,000", "10", "10", "8.97", "8.99"], ["10,000", "14", "14", "12.29", "12.39"],
       ["100,000", "17", "17", "15.61", "15.65"], ["1,000,000", "20", "20", "18.93", "18.99"]],
      [0.16, 0.24, 0.18, 0.24, 0.18], "Table 7.1 – Solution of the recurrence checked against the experiment (from Task 9)", T)

# ----------------------------------------------------------------- TASK 8
T = 8
h1("TASK 8 – Implement and Test the Algorithms (4 Marks)", T)
p("The three strategies are implemented in Python 3 in Task_8_Implementation_Testing/Source_Code/search_algorithms.py. The file "
  "contains linear_search, binary_search (recursive, with low and high parameters), build_hash and hash_search. The complete source "
  "is listed in Appendix A and a screenshot is shown in Figure 8.1.", T)
img(R("Report", "Source_Code_Screenshots", "Figure_S1_search_algorithms.png"), "Figure 8.1 – Screenshot of search_algorithms.py", T, 5.2)
p("**Testing procedure.** The file test_search.py runs eight deterministic tests and one randomised test. The deterministic tests "
  "cover the boundary cases (first, last and middle element, missing values, empty list, single element). The randomised test generates "
  "200 sorted lists of random size and checks that all three methods agree on every key.", T)
table(["#", "Test", "Result"],
      [["1", "Key at first position (0)", "PASS"], ["2", "Key at last position (999)", "PASS"], ["3", "Key in middle (500)", "PASS"],
       ["4", "Missing key (−1)", "PASS"], ["5", "Missing key (1000)", "PASS"], ["6", "Empty list returns −1", "PASS"],
       ["7", "Single element found", "PASS"], ["8", "Single element missing", "PASS"],
       ["9", "200 random sorted lists: all three methods agree", "PASS"]],
      [0.08, 0.72, 0.2], "Table 8.1 – Correctness test cases and results", T)
img(R("Report", "Output_Screenshots", "Figure_O1_correctness_tests.png"), "Figure 8.2 – Execution output of test_search.py (9 of 9 passed)", T, 5.6)
import sys as _sys
_sys.path.insert(0, R("Task_8_Implementation_Testing", "Source_Code"))
from search_algorithms import linear_search as _ls, binary_search as _bs, build_hash as _bh, hash_search as _hs
def _mids(n, key):
    lo, hi, seq = 0, n - 1, []
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        seq.append(mid)
        if mid == key:
            break
        lo, hi = (lo, mid - 1) if key < mid else (mid + 1, hi)
    return seq
_seq = _mids(1000, 999)
table(["Method", "Work performed for n = 1,000, key = 999", "Comparisons", "Result"],
      [["Linear Search", "Examines A[0] to A[999] in turn", str(_ls(list(range(1000)), 999)), "index 999"],
       ["Recursive Binary Search", "Checks mid = " + ", ".join(str(m) for m in _seq), str(len(_seq)), "index " + str(_bs(list(range(1000)), 999, 0, 999))],
       ["Hash Lookup", "One hash computation, one key check", "1", "index " + str(_hs(_bh(list(range(1000))), 999))]],
      [0.2, 0.46, 0.14, 0.2], "Table 8.2 – Trace of the three methods on the 1,000-record example (key 999)", T)
table(["Step", "low", "high", "mid", "A[mid]", "Decision"],
      [["1", "0", "9", "4", "4", "7 > 4, so low = mid + 1 = 5"], ["2", "5", "9", "7", "7", "equal: found at index 7"]],
      [0.1, 0.1, 0.1, 0.1, 0.1, 0.5], "Table 8.3 – Hand trace of binary search for n = 10, key = 7 (matches the program)", T)
p("The experiment program (Task 9) also cross-checks its own results: every binary and hash result is verified against the key, "
  "and the linear result against the known position, so a wrong answer would stop the run.", T)

# ----------------------------------------------------------------- TASK 9
T = 9
h1("TASK 9 – Record Experimental Performance (3 Marks)", T)
p("**Method.** The records are the sorted registration numbers 0 to n−1 for n = 1,000; 10,000; 100,000 and 1,000,000. The Linear "
  "Search target is the last record (worst successful case) and is timed as the mean of repeated calls. Binary and hash lookups are "
  "averaged over 1,000 random keys. The hash table is built once and its build time is recorded separately. Times use "
  "time.perf_counter(). The program is Task_9_Experimental_Performance/run_experiments.py and its output is in Figure 9.2.", T)
p("**Environment.** Python 3.12.3 on Linux (x86-64), Intel Xeon processor at 2.10 GHz, 1 virtual CPU, 4 GB RAM (cloud virtual machine). "
  "Results depend on the machine, so they are reported with their context.", T)
table(["n", "Linear: comparisons (worst)", "Linear: time (ms)", "Binary: comparisons (average)", "Binary: time (ms per search)", "Hash: build (ms)", "Hash: time (ms per lookup)"],
      [["1,000", "1,000", "0.0224", "8.99", "0.00088", "0.064", "0.000051"],
       ["10,000", "10,000", "0.2369", "12.39", "0.00136", "0.717", "0.000055"],
       ["100,000", "100,000", "2.6649", "15.65", "0.00258", "14.363", "0.000108"],
       ["1,000,000", "1,000,000", "24.4670", "18.99", "0.00332", "101.897", "0.000124"]],
      [0.13, 0.15, 0.13, 0.16, 0.16, 0.12, 0.15], "Table 9.1 – Measured results (Task_9 run, Report/Tables_and_Graphs/experimental_results.csv)", T)
p("For reference, Table 9.2 gives the illustrative measurements supplied in the assignment text. They have the same trends as the "
  "measured values in Table 9.1 (Linear Search is roughly linear in n, Binary Search is very small, and Hash Lookup is fastest). The "
  "measured values are used for all analysis in this report.", T)
table(["n", "Linear (ms)", "Recursive Binary (ms per search)", "Hash (ms per lookup)"],
      [["1,000", "0.032", "0.001318", "0.000106"], ["10,000", "0.496", "0.002072", "0.000055"],
       ["100,000", "3.557", "0.002664", "0.000059"], ["1,000,000", "40.813", "0.002758", "0.000105"]],
      [0.22, 0.24, 0.30, 0.24], "Table 9.2 – Illustrative measurements supplied in the assignment text", T)
img(R("Report", "Tables_and_Graphs", "performance_graphs.png"), "Figure 9.1 – Operation counts (left) and measured time per search (right); both axes logarithmic", T, 6.2)
img(R("Report", "Output_Screenshots", "Figure_O2_experiment_output.png"), "Figure 9.2 – Execution output of run_experiments.py", T, 5.6)
_rt = list(csv.DictReader(open(R("Report", "Tables_and_Graphs", "repeated_trials.csv"))))
_fmt = lambda m, sd, d=5: f"{float(m):.{d}f} ± {float(sd):.{d}f}"
table(["n", "Linear (ms)", "Binary (ms per search)", "Hash (ms per lookup)", "Binary average comparisons"],
      [[f"{int(r['n']):,}", _fmt(r['linear_mean_ms'], r['linear_sd_ms'], 4), _fmt(r['binary_mean_ms'], r['binary_sd_ms'], 6),
        _fmt(r['hash_mean_ms'], r['hash_sd_ms'], 6), r['binary_avg_comparisons']] for r in _rt],
      [0.14, 0.22, 0.22, 0.22, 0.2], "Table 9.3 – Mean ± standard deviation over 5 independent trials (repeated_trials.csv)", T)
p("Table 9.3 repeats the timing five times for every size. The first run (Table 9.1) and the trial means differ by up to about 20 % "
  "for Linear Search, because the cloud machine's speed varies from one run to the next. For this reason the analysis in this report "
  "relies on operation counts and on orders of magnitude, not on any single timing. The standard deviations are small compared with "
  "the differences between methods.", T)
img(R("Report", "Tables_and_Graphs", "repeated_trials_errorbars.png"), "Figure 9.3 – Mean time per search with ±1 standard deviation over 5 trials", T, 6.2)
p("**Interpretation.** Linear Search time rises by about a factor of 1,000 when n grows by a factor of 1,000, as expected for a Θ(n) "
  "method. Binary Search time rises only from 0.0009 ms to 0.0033 ms. Hash lookup stays between 0.00005 ms and 0.00012 ms, and the "
  "one-off hash build (about 102 ms at a million records) is the price of that speed.", T)

# ----------------------------------------------------------------- TASK 10
T = 10
h1("TASK 10 – Compare Theory with Experimental Behaviour (4 Marks)", T)
table(["Quantity", "Theoretical prediction", "Observed", "Agreement"],
      [["Linear worst-case comparisons", "n", "1,000 to 1,000,000 (exact)", "Exact"],
       ["Linear time ratio, 1M vs 1k", "1,000 (linear)", "1,094", "Close (≈ 9% above)"],
       ["Binary worst-case comparisons", "floor(log2 n) + 1 = 10, 14, 17, 20", "10, 14, 17, 20", "Exact"],
       ["Binary average comparisons", "log2 n − 1 = 8.97, 12.29, 15.61, 18.93", "8.99, 12.39, 15.65, 18.99", "Within 0.1 comparison"],
       ["Binary time ratio, 1M vs 1k", "≈ 2.0 (log n ratio)", "3.76", "Not matched; see text"],
       ["Hash lookup probes", "Θ(1), about 1", "1 key access per query", "Consistent"],
       ["Hash lookup time, 1k to 1M", "Nearly constant", "0.051 to 0.124 µs (≈ 2.4× for 1000× data)", "Consistent"],
       ["Hash build time, 1k to 1M", "Θ(n): ×1,000", "0.064 to 101.9 ms (×1,590)", "Consistent (cache and resizing overheads)"],
       ["Sort time, 1k to 1M", "Θ(n log n): ×2,000", "0.096 to 228.9 ms (×2,385)", "Consistent (overheads at large n)"]],
      [0.26, 0.26, 0.26, 0.22], "Table 10.1 – Predicted and observed behaviour", T)
p("**Where theory and measurement agree.** The operation counts match the mathematics exactly for Linear and Binary Search. Both "
  "the worst-case binary count and the linear count are exact integers, and the average binary count is within a tenth of a comparison "
  "of log2 n − 1. This is the strongest evidence in the report, because counts do not depend on the machine.", T)
p("**Where theory and measurement differ.** The time ratio for Binary Search is 3.76 rather than the 2.0 predicted by log n. The "
  "reasons are: (i) each level of the search is a Python function call, which costs far more than the single comparison counted in the "
  "theory, so the fixed cost per search dominates at small n; (ii) at large n the array of a million integers and the dictionary are "
  "larger than the CPU cache, so each access at deeper levels can miss the cache; (iii) the timer resolution and system noise are "
  "significant for measurements of a few microseconds. These effects change the constant factor, not the growth class: the times "
  "still grow far more slowly than n.", T)
_r1 = {int(r['n']): r for r in csv.DictReader(open(R("Report", "Tables_and_Graphs", "experimental_results.csv")))}
_rtm = {int(r['n']): r for r in _rt}
_lf = float(_r1[1000000]['linear_worst_ms']) / float(_r1[1000]['linear_worst_ms'])
_lm = float(_rtm[1000000]['linear_mean_ms']) / float(_rtm[1000]['linear_mean_ms'])
_bf = float(_r1[1000000]['binary_ms']) / float(_r1[1000]['binary_ms'])
_bm = float(_rtm[1000000]['binary_mean_ms']) / float(_rtm[1000]['binary_mean_ms'])
_hf = float(_r1[1000000]['hash_ms']) / float(_r1[1000]['hash_ms'])
_hm = float(_rtm[1000000]['hash_mean_ms']) / float(_rtm[1000]['hash_mean_ms'])
table(["Ratio, 1,000,000 vs 1,000 records", "Theory", "First run", "Mean of 5 trials"],
      [["Linear time", "1,000", f"{_lf:,.0f}", f"{_lm:,.0f}"],
       ["Binary time", "about 2.0 (log n)", f"{_bf:.2f}", f"{_bm:.2f}"],
       ["Hash lookup time", "about 1", f"{_hf:.2f}", f"{_hm:.2f}"]],
      [0.4, 0.2, 0.2, 0.2], "Table 10.2 – Time ratios from the two independent measurements", T)
p("Linear Search is between about 800 and 1,100 times slower at a million records, against a prediction of 1,000. Binary Search is "
  "slower than log n predicts, and its ratio varies most between runs, because its per-search time is only a few microseconds and is "
  "affected by timer resolution and call overhead. Hash lookup changes by a small factor at all sizes, as expected for a constant-time method.", T)
p("**Conclusion.** The experiments support the growth-rate analysis: Linear Search is Θ(n), Binary Search is Θ(log n) and Hash "
  "lookup is Θ(1) on average. Exact times should not be generalised to other machines, so the system should be re-measured on its "
  "target hardware before deployment.", T)

# ----------------------------------------------------------------- TASK 11
T = 11
h1("TASK 11 – Recommend and Defend the Final Design (4 Marks)", T)
p("**Recommendation.** Use a hash table keyed by the unique registration number, storing a reference to each student record. Hash "
  "lookup has the lowest cost per query, and the one-off preprocessing is small compared with the number of searches the system performs.", T)
p("**Technical justification.** At one million records the measured costs per search are: Linear Search 24.47 ms; Binary Search "
  "0.00332 ms; Hash lookup 0.000124 ms. The hash lookup is about 27 times faster than Binary Search and roughly 200,000 times faster "
  "than Linear Search (first run). Preparing the index also costs less than preparing the sorted order that Binary Search needs (102 ms for the "
  "hash table against 229 ms for sorting).", T)
p("**Break-even analysis.** Let q be the number of searches. Compared with Linear Search, the hash table repays its 102 ms build after "
  "about 4 searches. Compared with Binary Search on data that is already sorted, the hash table repays its build after about 31,900 "
  "searches. The system performs many more searches than this in a day, so the hash table is the better choice. If the records were "
  "unsorted, Binary Search would also need the sort, and the hash table is faster in every case.", T)
_crit = [("Lookup speed", .40, 1, 4, 5), ("Update cost (daily inserts)", .15, 5, 2, 4), ("Memory", .10, 5, 5, 3),
         ("Range queries", .05, 3, 5, 1), ("Preprocessing", .10, 5, 2, 3), ("Simplicity", .20, 5, 4, 3)]
_L = sum(c[1] * c[2] for c in _crit); _Bn = sum(c[1] * c[3] for c in _crit); _H = sum(c[1] * c[4] for c in _crit)
table(["Criterion", "Weight", "Linear", "Binary", "Hash"],
      [[c[0], f"{c[1]:.0%}", str(c[2]), str(c[3]), str(c[4])] for c in _crit] +
      [["Weighted total (out of 5)", "100%", f"{_L:.2f}", f"{_Bn:.2f}", f"{_H:.2f}"]],
      [0.4, 0.14, 0.15, 0.15, 0.16], "Table 11.1 – Weighted decision matrix (scores 1 to 5; weights are the assumptions stated in the text)", T)
p("The scores are judgements based on the measurements and on the requirement that a record be retrieved quickly from a registration number. "
  "The weights reflect that requirement, so lookup speed carries the largest weight. The result is sensitive to that weight: keeping the other "
  "weights in the same proportions, Hash is the highest-scoring method only while lookup speed carries at least about 26 % of the total. "
  "Below that, Binary Search is the better choice. This threshold is the point to discuss with the design team if the requirements change.", T)
p("**Trade-offs.** (1) The hash table needs extra memory proportional to n: measured with tracemalloc, a hash table of one million records used about 70 MB, against about 40 MB for a sorted list of the same integers. (2) Its worst case is O(n) if many keys collide; "
  "a good hash function and resizing when the load factor grows keep this unlikely. (3) Hash tables do not support ordered queries "
  "such as 'all students with registration numbers between X and Y'. (4) Daily additions, updates and deletions must keep the "
  "index consistent with the database. Insertion is expected O(1), and rebuilding the whole index takes about 0.1 s, so a daily rebuild is practical.", T)
p("**When the other methods would be preferred.** Binary Search is better when memory is tightly limited, when ordered output or range "
  "queries are needed, or when there are very few searches on data that is already sorted. Linear Search is adequate only for very small "
  "lists (for example a few hundred records) or for occasional searches on unsorted data, where its simplicity outweighs its cost.", T)

# ----------------------------------------------------------------- TASK 12
T = 12
h1("TASK 12 – Day-4 Design Challenge (8 Marks)", T)
h2("A. Impact Analysis (2 Marks)", T)
p("The revised system holds 1,000,000 records and must handle 50,000 searches per hour, which is an average of 13.9 searches per second. "
  "New records arrive once per day, so preprocessing can be performed once and reused across many queries. Table 12.1 converts the "
  "measured per-search costs into the total work per hour.", T)
h2("B. Evaluation of the Original Design (2 Marks)", T)
p("The hash table remains suitable. Building it once takes expected Θ(n) time, and each query takes expected Θ(1) time. The cost of "
  "the hour is therefore proportional to the number of requests, not to one million records per request. Binary Search also works "
  "if the data is kept sorted, but it performs about 20 comparisons per query and cannot answer as quickly. Linear Search would inspect "
  "up to one million keys per request and is clearly unsuitable.", T)
table(["Strategy", "One-off preparation", "Work for 50,000 searches", "Total per hour", "Share of one CPU core"],
      [["Linear Search (worst-case keys)", "None", "50,000 × 24.47 ms = 1,223 s", "About 20.4 min", "About 34 %"],
       ["Linear Search (average keys, about n/2)", "None", "About 612 s", "About 10.2 min", "About 17 %"],
       ["Binary Search (sort once, reused)", "229 ms sort", "50,000 × 0.00332 ms = 166 ms", "About 0.39 s", "About 0.01 %"],
       ["Hash table (build once, reused)", "102 ms build", "50,000 × 0.000124 ms = 6.2 ms", "About 0.11 s", "About 0.003 %"]],
      [0.31, 0.16, 0.25, 0.14, 0.14], "Table 12.1 – Total work per hour at 1,000,000 records (from Table 9.1)", T)
h2("C. Adaptation or Redesign (2 Marks)", T)
p("**Decision: MODIFY the design and keep the hash-table strategy as a persistent registration-number index.** Build the index at start-up "
  "(or load it from a durable snapshot) and insert each day's new records as they arrive. Use a collision-handling scheme, monitor the load "
  "factor and resize when it grows. Keep the database authoritative and update the index in the same transaction as the record, so that "
  "the index never points to a record that no longer exists.", T)
p("**Complexity of the revised design.** The initial build costs expected Θ(n), each insertion expected Θ(1) and each search expected Θ(1). "
  "If a complete rebuild is performed daily, its Θ(n) cost (about 0.1 s) is spread over 50,000 requests per hour and many more over the day. "
  "The worst case remains O(n) if collisions are extreme, which a good hash function makes very unlikely.", T)
h2("D. Evidence-Based Defence (2 Marks)", T)
p("Table 12.1 shows the measured evidence. At one million records, Linear Search would consume about a third of one CPU core every "
  "hour with worst-case keys (about a sixth on average), and its cost would rise by a factor of 1,000 if the database grew to a billion records. Binary "
  "Search needs about 20 comparisons per query and is comfortably fast, and the hash table is faster still: its per-query work is about 4 % of "
  "the Binary Search work (6.2 ms against 166 ms), and about 27 % including its build. These are measured values on a single test machine, not guarantees for the production system.", T)
p("The hash table is therefore preferred. Binary Search is a strong alternative when ordered output or range queries are required, and "
  "the two can be combined: a hash index for exact look-up and a sorted copy for range queries.", T)

# ----------------------------------------------------------------- CONCLUSION
_m = _rtm[1000000]
_lin_min = 50000 * float(_m['linear_mean_ms']) / 1000 / 60
_bin_s = (float(_r1[1000000]['sort_ms']) + 50000 * float(_m['binary_mean_ms'])) / 1000
_hash_s = (float(_r1[1000000]['hash_build_ms']) + 50000 * float(_m['hash_mean_ms'])) / 1000
h2("E. Sensitivity to Measurement Variability (2 Marks)", T)
p("Table 12.2 repeats the hour totals using the mean of the five trials for the cost of each search. The one-off sort and hash build "
  "are taken from the first run, because the repeated study measured the searches only.", T)
table(["Strategy", "Work for 50,000 searches (trial mean)", "Total per hour"],
      [["Linear Search (worst-case keys)", f"50,000 × {float(_m['linear_mean_ms']):.2f} ms", f"About {_lin_min:.1f} min"],
       ["Binary Search (sort once, reused)", f"{float(_r1[1000000]['sort_ms']):.0f} ms sort + 50,000 × {float(_m['binary_mean_ms']):.4f} ms", f"About {_bin_s:.2f} s"],
       ["Hash table (build once, reused)", f"{float(_r1[1000000]['hash_build_ms']):.0f} ms build + 50,000 × {float(_m['hash_mean_ms']):.6f} ms", f"About {_hash_s:.2f} s"]],
      [0.34, 0.44, 0.22], "Table 12.2 – Hour totals at 1,000,000 records using trial means for the query cost", T)
p("The conclusion is unchanged. Linear Search would occupy a CPU core for many minutes every hour, while the indexed approaches "
  "finish their work in well under a second. The hash table remains the lowest-cost option in both sets of figures.", T)

h1("Limitations and Threats to Validity")
p("The conclusions of this study are subject to the following limitations, which are stated so that the reader can judge how far they apply.")
bul([
 "**Single environment.** All measurements come from one cloud virtual machine (2.10 GHz Intel Xeon, one vCPU). Absolute times will differ on other hardware. The growth classes and operation counts do not depend on the machine.",
 "**Timing variability.** Single runs differ by up to about 20 % for Linear Search (Table 9.1 against Table 9.3). The report therefore uses means of five trials where timings matter, and relies on orders of magnitude.",
 "**Interpreter overhead.** Python adds a fixed cost to every function call and loop iteration. This raises the constants, especially for Binary Search, whose per-search cost is only a few microseconds. A compiled implementation would be faster, with the same growth classes.",
 "**Test keys were sequential integers.** The records were the integers 0 to n−1. Python's hash of a small integer is the integer itself, so these keys are spread perfectly across the table. Real registration numbers (for example, strings such as '192511397') are hashed differently and may collide more. The hash results in this report are therefore a best case, and the system should be tested with the real key format.",
 "**Query distribution.** Query keys were chosen uniformly at random. If some students are searched far more often than others, the cache behaviour and the average costs will differ.",
 "**Few sizes.** Only four record counts (1,000 to 1,000,000) were measured. Growth between them was assumed from the theory, not measured directly.",
 "**Memory.** Memory was measured once with tracemalloc for one million records, so the memory figures are indicative only.",
])

h1("Conclusion")
p("This assignment compared iterative Linear Search, Recursive Binary Search and Hash-Table Lookup. Linear Search is simple but scales "
  "linearly: Θ(n) comparisons per search, and 24.5 ms per search at one million records. Binary Search needs sorted records, but then "
  "uses floor(log2 n) + 1 comparisons in the worst case, which is 20 for a million records. A hash table costs expected Θ(n) to build and "
  "answers each lookup in expected Θ(1), which is the best fit for the revised workload of one million records, frequent searches and "
  "daily updates. The operation counts match the theory exactly, and the timings show the same growth patterns. The timings should be "
  "re-measured on the target system before deployment.")

# ----------------------------------------------------------------- REFERENCES
h1("References")
bul(["T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, Introduction to Algorithms, 4th ed., MIT Press, 2022.",
     "Python Software Foundation, Python 3 Documentation: built-in types (list and dict), https://docs.python.org/3/.",
     "CSA06 Design and Analysis of Algorithms, Assignment 1 – CO1, course assignment sheet."])

# ----------------------------------------------------------------- APPENDIX A
h1("Appendix A – Source Code")
p("The complete runnable source is in the Task_8_Implementation_Testing/Source_Code and Task_9_Experimental_Performance folders. "
  "Run the tests with: python test_search.py. Run the experiments with: python run_experiments.py (from the CO1_Assignment folder).")
h2("A.1 search_algorithms.py")
code(open(R("Task_8_Implementation_Testing", "Source_Code", "search_algorithms.py")).read().rstrip())
h2("A.2 test_search.py")
code(open(R("Task_8_Implementation_Testing", "Source_Code", "test_search.py")).read().rstrip())
h2("A.3 run_experiments.py")
code(open(R("Task_9_Experimental_Performance", "run_experiments.py")).read().rstrip())

# ----------------------------------------------------------------- APPENDIX B
h1("Appendix B – Raw Experimental Data")
p("Source: Report/Tables_and_Graphs/experimental_results.csv, written by run_experiments.py. Times in milliseconds.")
import csv
rows = list(csv.DictReader(open(R("Report", "Tables_and_Graphs", "experimental_results.csv"))))
keys = ["n", "linear_worst_comparisons", "linear_worst_ms", "binary_avg_comparisons", "binary_worst_comparisons", "binary_ms", "hash_build_ms", "hash_ms", "sort_ms"]
hdr = ["n", "Linear cmp", "Linear ms", "Binary avg cmp", "Binary worst cmp", "Binary ms", "Hash build ms", "Hash ms", "Sort ms"]
table(hdr, [[r[k] for k in keys] for r in rows], [0.1, 0.11, 0.11, 0.12, 0.12, 0.11, 0.11, 0.11, 0.11],
      "Table B.1 – Raw measurements (experimental_results.csv)")
table(["n", "Linear mean ms", "Linear SD", "Binary mean ms", "Binary SD", "Hash mean ms", "Hash SD"],
      [[f"{int(r['n']):,}", r['linear_mean_ms'], r['linear_sd_ms'], r['binary_mean_ms'], r['binary_sd_ms'], r['hash_mean_ms'], r['hash_sd_ms']] for r in _rt],
      [0.13, 0.145, 0.145, 0.145, 0.145, 0.145, 0.145],
      "Table B.2 – Repeated trials, five per size (repeated_trials.csv)")

h1("Appendix C – Glossary")
table(["Term", "Meaning in this report"],
      [["Basic operation", "The operation whose count determines the running time (here, a key comparison or a hash lookup)."],
       ["Θ, O, Ω", "Tight, upper and lower asymptotic bounds on the growth of a function (Task 5)."],
       ["Recurrence", "An equation that defines a function in terms of its value on smaller inputs (Tasks 6 and 7)."],
       ["Load factor α", "Number of stored keys divided by the number of hash buckets. Lookup cost stays constant while α is kept bounded."],
       ["Collision", "Two different keys mapped to the same hash bucket or slot."],
       ["Preprocessing", "Work done once before the searches, such as sorting or building the hash table."],
       ["Standard deviation (SD)", "A measure of the spread of repeated timings; a small SD means the timings are consistent."],
       ["tracemalloc", "The Python module used to measure the memory allocated by the program."]],
      [0.28, 0.72], "Table C.1 – Glossary of terms")

COVER = {
    "lines": [
        ("SIMATS ENGINEERING", 30, True),
        ("Department of Computer Science and Engineering", 24, False),
        ("", 20, False),
        ("CSA06 – DESIGN AND ANALYSIS OF ALGORITHMS", 26, True),
        ("ASSIGNMENT 1 – CO1", 26, True),
        ("", 20, False),
        ("Design, Analyse and Validate an Efficient Search Strategy", 26, True),
        ("for a Large-Scale Student Record System", 26, True),
        ("", 20, False),
    ],
    "fields": [("Student Name", "SARAVANAH"), ("Register Number", "192511397"),
               ("Course Outcome", "Determine algorithm efficiency using asymptotic notations and mathematical techniques."),
               ("Academic Year", "2026–2027")],
}
json.dump({"cover": COVER, "blocks": B}, open(os.path.join(os.path.dirname(__file__), "content.json"), "w"), ensure_ascii=False, indent=1)
print("blocks:", len(B))
