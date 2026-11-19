## TASK 1 – Design the Algorithms (5 Marks)

### 1. Iterative Linear Search

**Basic idea.** Inspect each registration number from the beginning until the key is found or the list ends. It needs no sorting, so it is the baseline for unsorted records.

```
LINEAR-SEARCH(A, key)
    for i = 0 to length(A) - 1
        if A[i] == key
            return i
    return -1
```

### 2. Recursive Binary Search

**Basic idea.** Search a sorted array by comparing the key with the middle element. If the key is smaller, search only the left half; if larger, only the right half. Each call discards about half of the remaining candidates. The records must be sorted beforehand; a comparison sort costs O(n log n).

```
BINARY-SEARCH(A, key, low, high)
    if low > high: return -1
    mid = low + (high - low) // 2
    if A[mid] == key: return mid
    if key < A[mid]:
        return BINARY-SEARCH(A, key, low, mid - 1)
    return BINARY-SEARCH(A, key, mid + 1, high)
```

The midpoint is computed as low + (high − low) // 2 rather than (low + high) // 2. The two are equal in mathematics, but the first form cannot overflow in fixed-width integer languages, which is good practice for an index calculation.

### 3. Hash-Table Lookup

**Basic idea.** Store each registration number as a key in a hash table. A hash function maps the key to a slot or bucket. Building the table is preprocessing that takes expected O(n) time; a lookup takes expected O(1) time when collisions are controlled.

```
BUILD-HASH(records)
    create empty hash table H
    for each record r in records:
        H[r.registration_number] = r
    return H

HASH-SEARCH(H, key)
    if key is in H: return H[key]
    return NOT-FOUND
```

Hash-table lookup differs from the two comparison-based methods. Its expected cost depends on the hash function and the load factor rather than on the number of comparisons with keys, and its worst case (all keys in one bucket) degrades to O(n).

**Design summary.** Linear Search trades speed for simplicity and needs no preprocessing. Binary Search needs sorted data but uses very few comparisons. Hash lookup spends extra time and memory on an index, then answers each query in almost constant time.
