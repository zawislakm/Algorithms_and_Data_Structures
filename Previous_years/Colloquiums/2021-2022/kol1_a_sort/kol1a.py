from kol1atesty import runtests
from typing import List

"""
Algorithm starts by sorting words by their length, same as in bucket sort. During putting words in buckets word that
last letter is smaller (first in alphabet) than first letter is reversed. Then all buckets are sorted using radix sort. 
All same words now are next to each other. They are counted in linear way in buckets.
"""


def counting_sort(A: List[str], index: int) -> None:
    n = len(A)
    k = 26
    C = [0 for _ in range(k)]
    B = [None for _ in range(n)]

    for i in range(n):
        C[ord(A[i][index]) - 97] += 1

    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[ord(A[i][index]) - 97] -= 1
        B[C[ord(A[i][index]) - 97]] = A[i]

    for i in range(n):
        A[i] = B[i]


def radix_sort(A: List[str], words_length: int) -> None:
    for i in range(words_length - 1, -1, -1):
        counting_sort(A, i)


def strong_string(T: List[str]) -> int:
    n = max(len(t) for t in T) + 1
    buckets = [[] for _ in range(n)]

    for t in T:
        if t[0] > t[-1]:
            buckets[len(t)].append(t[::-1])
        else:
            buckets[len(t)].append(t)

    for bucket in buckets:
        if len(bucket) > 2:  # no point to sort [],['str'],['str','rts']
            radix_sort(bucket, len(bucket[0]))

    ans = 0
    for bucket in buckets:
        if len(bucket) >= 1 and len(bucket) > ans:
            count = 1
            check = bucket[0]
            for t in bucket[1:]:
                if t == check:
                    count += 1
                else:
                    ans = max(ans, count)
                    count = 1
                    check = t
            ans = max(ans, count)
    return ans


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
