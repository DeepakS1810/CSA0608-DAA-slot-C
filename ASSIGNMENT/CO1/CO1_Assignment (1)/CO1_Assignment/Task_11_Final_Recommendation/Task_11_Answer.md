## TASK 11 – Recommend and Defend the Final Design (4 Marks)

**Recommendation.** Use a hash table keyed by the unique registration number, storing a reference to each student record. Hash lookup has the lowest cost per query, and the one-off preprocessing is small compared with the number of searches the system performs.

**Technical justification.** At one million records the measured costs per search are: Linear Search 24.47 ms; Binary Search 0.00332 ms; Hash lookup 0.000124 ms. The hash lookup is about 27 times faster than Binary Search and roughly 200,000 times faster than Linear Search (first run). Preparing the index also costs less than preparing the sorted order that Binary Search needs (102 ms for the hash table against 229 ms for sorting).

**Break-even analysis.** Let q be the number of searches. Compared with Linear Search, the hash table repays its 102 ms build after about 4 searches. Compared with Binary Search on data that is already sorted, the hash table repays its build after about 31,900 searches. The system performs many more searches than this in a day, so the hash table is the better choice. If the records were unsorted, Binary Search would also need the sort, and the hash table is faster in every case.

| Criterion | Weight | Linear | Binary | Hash |
|---|---|---|---|---|
| Lookup speed | 40% | 1 | 4 | 5 |
| Update cost (daily inserts) | 15% | 5 | 2 | 4 |
| Memory | 10% | 5 | 5 | 3 |
| Range queries | 5% | 3 | 5 | 1 |
| Preprocessing | 10% | 5 | 2 | 3 |
| Simplicity | 20% | 5 | 4 | 3 |
| Weighted total (out of 5) | 100% | 3.30 | 3.65 | 3.85 |

*Table 11.1 – Weighted decision matrix (scores 1 to 5; weights are the assumptions stated in the text)*

The scores are judgements based on the measurements and on the requirement that a record be retrieved quickly from a registration number. The weights reflect that requirement, so lookup speed carries the largest weight. The result is sensitive to that weight: keeping the other weights in the same proportions, Hash is the highest-scoring method only while lookup speed carries at least about 26 % of the total. Below that, Binary Search is the better choice. This threshold is the point to discuss with the design team if the requirements change.

**Trade-offs.** (1) The hash table needs extra memory proportional to n: measured with tracemalloc, a hash table of one million records used about 70 MB, against about 40 MB for a sorted list of the same integers. (2) Its worst case is O(n) if many keys collide; a good hash function and resizing when the load factor grows keep this unlikely. (3) Hash tables do not support ordered queries such as 'all students with registration numbers between X and Y'. (4) Daily additions, updates and deletions must keep the index consistent with the database. Insertion is expected O(1), and rebuilding the whole index takes about 0.1 s, so a daily rebuild is practical.

**When the other methods would be preferred.** Binary Search is better when memory is tightly limited, when ordered output or range queries are needed, or when there are very few searches on data that is already sorted. Linear Search is adequate only for very small lists (for example a few hundred records) or for occasional searches on unsorted data, where its simplicity outweighs its cost.
