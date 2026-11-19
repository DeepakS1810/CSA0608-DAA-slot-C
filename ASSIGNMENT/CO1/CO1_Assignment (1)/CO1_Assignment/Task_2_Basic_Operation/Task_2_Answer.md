## TASK 2 – Identify the Basic Operation (2 Marks)

The basic operation is the operation that is executed most often and therefore determines the count of work. In all three algorithms it is the comparison of the search key with a stored registration number. Other steps (loop increments, computing mid, returning a value) take a fixed amount of time per iteration and do not change the order of growth.

| Algorithm | Basic operation | Why this is the basic operation | Count behaviour |
|---|---|---|---|
| Linear Search | Equality test A[i] == key | Executed once for each record examined; it is the only work inside the loop | One test per examined record: 1 to n |
| Recursive Binary Search | Comparison of key with A[mid] | Executed once per recursive call; the call itself and the mid calculation are constant extra work | One comparison per level; the interval halves each time |
| Hash Lookup | Hash calculation h(key) and key check in the selected slot | Each lookup performs one hash calculation and at most a few key checks in its bucket | Expected a constant number of checks; heavy collisions can force many |

*Table 2.1 – Basic operations of the three strategies*

In the Python program (Task 8) the counts used for Linear and Binary Search are key comparisons, and the Hash lookup is one dictionary access, which Python performs with one hash computation and expected one key check.
