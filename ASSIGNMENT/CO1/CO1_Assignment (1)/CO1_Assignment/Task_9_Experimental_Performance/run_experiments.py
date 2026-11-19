"""
Experimental measurement of the three search strategies (Tasks 9 and 10).
Writes raw data to Report/Tables_and_Graphs/ and graphs to the same folder.
Run from the CO1_Assignment folder:  python Task_9_Experimental_Performance/run_experiments.py
"""
import csv, math, os, platform, random, statistics, sys, time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "Task_8_Implementation_Testing", "Source_Code"))
from search_algorithms import linear_search, binary_search, build_hash, hash_search

OUT = os.path.join(ROOT, "Report", "Tables_and_Graphs")
os.makedirs(OUT, exist_ok=True)
SIZES = [1_000, 10_000, 100_000, 1_000_000]
NUM_KEYS = 1000          # random keys used to average binary and hash searches
SEED = 2026


def count_linear(a, key):
    """Key comparisons made by the iterative linear search."""
    for c, v in enumerate(a, 1):
        if v == key:
            return c
    return len(a)


def count_binary(a, key):
    """Key comparisons made by recursive binary search (same decisions, counted)."""
    low, high, c = 0, len(a) - 1, 0
    while low <= high:
        mid = low + (high - low) // 2
        c += 1
        if a[mid] == key:
            return c
        if key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return c


def time_call(fn, repeats):
    """Mean seconds per call."""
    t0 = time.perf_counter()
    for _ in range(repeats):
        fn()
    return (time.perf_counter() - t0) / repeats


def run():
    rng = random.Random(SEED)
    rows = []
    print(f"Python {platform.python_version()} on {platform.platform()}")
    print(f"{'n':>10} {'Lin cmp':>10} {'Lin ms':>10} {'Bin avg cmp':>12} {'Bin ms':>10} "
          f"{'Hash build ms':>14} {'Hash ms':>10} {'Sort ms':>10}")
    for n in SIZES:
        records = list(range(n))                      # sorted, unique registration numbers
        worst_key = n - 1                             # last element: worst successful search
        keys = [rng.randrange(n) for _ in range(NUM_KEYS)]

        # --- Linear search (worst case, target at the end; repeated for stable timing)
        reps = max(3, 2_000_000 // n)
        t_lin = time_call(lambda: linear_search(records, worst_key), reps)
        lin_cmp = count_linear(records, worst_key)

        # --- Recursive binary search (average over random keys)
        t_bin = time_call(lambda: [binary_search(records, k, 0, n - 1) for k in keys], 3) / NUM_KEYS
        bin_counts = [count_binary(records, k) for k in keys]

        # --- Hash table: build once (preprocessing), then lookups
        t0 = time.perf_counter()
        table = build_hash(records)
        t_build = time.perf_counter() - t0
        t_hash = time_call(lambda: [hash_search(table, k) for k in keys], 20) / NUM_KEYS

        # --- Correctness cross-check on this dataset
        assert all(binary_search(records, k, 0, n - 1) == hash_search(table, k) == k for k in keys)
        assert linear_search(records, worst_key) == worst_key

        # --- Sorting cost (what Binary Search would need if the records were unsorted)
        shuffled = records[:]
        rng.shuffle(shuffled)
        t0 = time.perf_counter()
        sorted(shuffled)
        t_sort = time.perf_counter() - t0

        row = dict(n=n,
                   log2_n=round(math.log2(n), 2),
                   linear_worst_comparisons=lin_cmp,
                   linear_worst_ms=round(t_lin * 1e3, 5),
                   binary_avg_comparisons=round(statistics.mean(bin_counts), 2),
                   binary_worst_comparisons=max(bin_counts),
                   binary_ms=round(t_bin * 1e3, 6),
                   hash_build_ms=round(t_build * 1e3, 3),
                   hash_ms=round(t_hash * 1e3, 6),
                   sort_ms=round(t_sort * 1e3, 3))
        rows.append(row)
        print(f"{n:>10,} {lin_cmp:>10,} {t_lin*1e3:>10.4f} {row['binary_avg_comparisons']:>12.2f} "
              f"{t_bin*1e3:>10.5f} {t_build*1e3:>14.2f} {t_hash*1e3:>10.5f} {t_sort*1e3:>10.2f}")

    with open(os.path.join(OUT, "experimental_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    # ---- Graphs --------------------------------------------------------------
    n = [r["n"] for r in rows]
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.4))
    ax[0].plot(n, [r["linear_worst_comparisons"] for r in rows], "o-", color="#c0392b", label="Linear (worst case)")
    ax[0].plot(n, [r["binary_avg_comparisons"] for r in rows], "s-", color="#2471a3", label="Binary (average)")
    ax[0].plot(n, [r["log2_n"] for r in rows], ":", color="#2471a3", label="log2 n (reference)")
    ax[0].plot(n, [1 for _ in rows], "^-", color="#1e8449", label="Hash (expected, 1 probe)")
    ax[0].set_xscale("log"); ax[0].set_yscale("log")
    ax[0].set_xlabel("Number of records n"); ax[0].set_ylabel("Key comparisons per search")
    ax[0].set_title("Operation counts"); ax[0].legend(fontsize=8); ax[0].grid(alpha=.3)

    ax[1].plot(n, [r["linear_worst_ms"] for r in rows], "o-", color="#c0392b", label="Linear (worst case)")
    ax[1].plot(n, [r["binary_ms"] for r in rows], "s-", color="#2471a3", label="Binary (per search)")
    ax[1].plot(n, [r["hash_ms"] for r in rows], "^-", color="#1e8449", label="Hash (per lookup)")
    ax[1].set_xscale("log"); ax[1].set_yscale("log")
    ax[1].set_xlabel("Number of records n"); ax[1].set_ylabel("Time per search (ms)")
    ax[1].set_title("Measured time per search"); ax[1].legend(fontsize=8); ax[1].grid(alpha=.3)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "performance_graphs.png"), dpi=160)
    plt.close(fig)
    print("Saved results to", OUT)
    return rows


if __name__ == "__main__":
    run()
