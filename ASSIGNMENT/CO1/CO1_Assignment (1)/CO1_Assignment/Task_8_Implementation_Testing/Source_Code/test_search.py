"""Correctness tests for the three search strategies. Run: python test_search.py"""
import random
from search_algorithms import linear_search, binary_search, build_hash, hash_search


def bs(a, k):
    return binary_search(a, k, 0, len(a) - 1)


def run():
    results = []

    def check(name, cond):
        results.append(cond)
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")

    print("=== Correctness tests ===")
    a = list(range(1000))
    h = build_hash(a)
    check("key at first position (0)", linear_search(a, 0) == bs(a, 0) == hash_search(h, 0) == 0)
    check("key at last position (999)", linear_search(a, 999) == bs(a, 999) == hash_search(h, 999) == 999)
    check("key in middle (500)", linear_search(a, 500) == bs(a, 500) == hash_search(h, 500) == 500)
    check("missing key (-1)", linear_search(a, -1) == bs(a, -1) == hash_search(h, -1) == -1)
    check("missing key (1000)", linear_search(a, 1000) == bs(a, 1000) == hash_search(h, 1000) == -1)
    check("empty list returns -1", linear_search([], 5) == -1 and bs([], 5) == -1 and hash_search(build_hash([]), 5) == -1)
    check("single element found", bs([7], 7) == 0)
    check("single element missing", bs([7], 8) == -1)

    rng = random.Random(1)
    ok = True
    for _ in range(200):
        n = rng.randint(1, 300)
        a = sorted(rng.sample(range(10 * n), n))
        h = build_hash(a)
        for k in rng.sample(range(10 * n), 20):
            r1, r2, r3 = linear_search(a, k), bs(a, k), hash_search(h, k)
            ok &= (r1 == -1 and r2 == -1 and r3 == -1) or (a[r1] == k and a[r2] == k and a[r3] == k)
    check("200 random sorted lists: all three agree on found/missing", ok)
    print(f"RESULT: {sum(results)}/{len(results)} tests passed")
    return all(results)


if __name__ == "__main__":
    run()
