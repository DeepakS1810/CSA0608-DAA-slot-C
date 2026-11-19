"""Repeats the timing measurements 5 times per size and reports mean and standard deviation.
Run from the CO1_Assignment folder:  python Task_9_Experimental_Performance/repeat_trials.py"""
import csv, os, random, statistics, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_experiments import SIZES, time_call, count_linear, count_binary, NUM_KEYS, ROOT
sys.path.insert(0, os.path.join(ROOT, "Task_8_Implementation_Testing", "Source_Code"))
from search_algorithms import linear_search, binary_search, build_hash, hash_search

TRIALS = 5
rows = []
for n in SIZES:
    records = list(range(n))
    rng = random.Random(7)
    keys = [rng.randrange(n) for _ in range(NUM_KEYS)]
    table = build_hash(records)
    lin, bin_, hsh = [], [], []
    for _ in range(TRIALS):
        lin.append(time_call(lambda: linear_search(records, n - 1), max(3, 2_000_000 // n)) * 1e3)
        bin_.append(time_call(lambda: [binary_search(records, k, 0, n - 1) for k in keys], 3) / NUM_KEYS * 1e3)
        hsh.append(time_call(lambda: [hash_search(table, k) for k in keys], 20) / NUM_KEYS * 1e3)
    rows.append(dict(n=n,
                     linear_mean_ms=round(statistics.mean(lin), 5), linear_sd_ms=round(statistics.stdev(lin), 5),
                     binary_mean_ms=round(statistics.mean(bin_), 6), binary_sd_ms=round(statistics.stdev(bin_), 6),
                     hash_mean_ms=round(statistics.mean(hsh), 6), hash_sd_ms=round(statistics.stdev(hsh), 6),
                     binary_avg_comparisons=round(statistics.mean(count_binary(records, k) for k in keys), 2)))
    print(rows[-1])
out = os.path.join(ROOT, "Report", "Tables_and_Graphs", "repeated_trials.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print("saved", out)
