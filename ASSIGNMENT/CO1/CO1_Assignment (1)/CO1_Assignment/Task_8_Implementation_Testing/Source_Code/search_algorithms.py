"""
CSA06 Assignment 1 (CO1): Search strategies for a large-scale student record system.
Implements Linear Search (iterative), Recursive Binary Search and Hash-Table Lookup.
"""


def linear_search(records, key):
    """Iterative linear search. Returns index of key or -1. Basic operation: key comparison."""
    for i, value in enumerate(records):
        if value == key:
            return i
    return -1


def binary_search(records, key, low, high):
    """Recursive binary search on a SORTED list. Returns index or -1."""
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if records[mid] == key:
        return mid
    if key < records[mid]:
        return binary_search(records, key, low, mid - 1)
    return binary_search(records, key, mid + 1, high)


def build_hash(records):
    """Build a hash table mapping registration number -> index (expected O(n))."""
    return {value: i for i, value in enumerate(records)}


def hash_search(table, key):
    """Hash-table lookup. Expected O(1). Returns index or -1."""
    return table.get(key, -1)
