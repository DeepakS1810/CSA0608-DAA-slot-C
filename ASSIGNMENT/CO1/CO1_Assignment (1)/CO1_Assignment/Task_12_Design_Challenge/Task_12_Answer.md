## TASK 12 – Day-4 Design Challenge (8 Marks)

### A. Impact Analysis (2 Marks)

The revised system holds 1,000,000 records and must handle 50,000 searches per hour, which is an average of 13.9 searches per second. New records arrive once per day, so preprocessing can be performed once and reused across many queries. Table 12.1 converts the measured per-search costs into the total work per hour.

### B. Evaluation of the Original Design (2 Marks)

The hash table remains suitable. Building it once takes expected Θ(n) time, and each query takes expected Θ(1) time. The cost of the hour is therefore proportional to the number of requests, not to one million records per request. Binary Search also works if the data is kept sorted, but it performs about 20 comparisons per query and cannot answer as quickly. Linear Search would inspect up to one million keys per request and is clearly unsuitable.

| Strategy | One-off preparation | Work for 50,000 searches | Total per hour | Share of one CPU core |
|---|---|---|---|---|
| Linear Search (worst-case keys) | None | 50,000 × 24.47 ms = 1,223 s | About 20.4 min | About 34 % |
| Linear Search (average keys, about n/2) | None | About 612 s | About 10.2 min | About 17 % |
| Binary Search (sort once, reused) | 229 ms sort | 50,000 × 0.00332 ms = 166 ms | About 0.39 s | About 0.01 % |
| Hash table (build once, reused) | 102 ms build | 50,000 × 0.000124 ms = 6.2 ms | About 0.11 s | About 0.003 % |

*Table 12.1 – Total work per hour at 1,000,000 records (from Table 9.1)*

### C. Adaptation or Redesign (2 Marks)

**Decision: MODIFY the design and keep the hash-table strategy as a persistent registration-number index.** Build the index at start-up (or load it from a durable snapshot) and insert each day's new records as they arrive. Use a collision-handling scheme, monitor the load factor and resize when it grows. Keep the database authoritative and update the index in the same transaction as the record, so that the index never points to a record that no longer exists.

**Complexity of the revised design.** The initial build costs expected Θ(n), each insertion expected Θ(1) and each search expected Θ(1). If a complete rebuild is performed daily, its Θ(n) cost (about 0.1 s) is spread over 50,000 requests per hour and many more over the day. The worst case remains O(n) if collisions are extreme, which a good hash function makes very unlikely.

### D. Evidence-Based Defence (2 Marks)

Table 12.1 shows the measured evidence. At one million records, Linear Search would consume about a third of one CPU core every hour with worst-case keys (about a sixth on average), and its cost would rise by a factor of 1,000 if the database grew to a billion records. Binary Search needs about 20 comparisons per query and is comfortably fast, and the hash table is faster still: its per-query work is about 4 % of the Binary Search work (6.2 ms against 166 ms), and about 27 % including its build. These are measured values on a single test machine, not guarantees for the production system.

The hash table is therefore preferred. Binary Search is a strong alternative when ordered output or range queries are required, and the two can be combined: a hash index for exact look-up and a sorted copy for range queries.

### E. Sensitivity to Measurement Variability (2 Marks)

Table 12.2 repeats the hour totals using the mean of the five trials for the cost of each search. The one-off sort and hash build are taken from the first run, because the repeated study measured the searches only.

| Strategy | Work for 50,000 searches (trial mean) | Total per hour |
|---|---|---|
| Linear Search (worst-case keys) | 50,000 × 20.17 ms | About 16.8 min |
| Binary Search (sort once, reused) | 229 ms sort + 50,000 × 0.0026 ms | About 0.36 s |
| Hash table (build once, reused) | 102 ms build + 50,000 × 0.000104 ms | About 0.11 s |

*Table 12.2 – Hour totals at 1,000,000 records using trial means for the query cost*

The conclusion is unchanged. Linear Search would occupy a CPU core for many minutes every hour, while the indexed approaches finish their work in well under a second. The hash table remains the lowest-cost option in both sets of figures.
