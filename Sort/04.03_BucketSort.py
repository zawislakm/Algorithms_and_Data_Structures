from typing import List


# n

def insertion_sort(A: List[int]) -> List[int]:
    n = len(A)

    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and key <= A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

    return A


def bucketsort(A: List[int]) -> None:
    n = len(A)
    min_e = min(A)
    max_e = max(A)
    if min_e == max_e:
        return

    buckets = [[] for _ in range(n + 1)]

    for x in A:
        num_bucket = int((x - min_e) / (max_e - min_e) * n)
        buckets[num_bucket].append(x)

    for bucket in buckets:
        insertion_sort(bucket)

    k = 0
    for bucket in buckets:
        for x in bucket:
            A[k] = x
            k += 1


arr = [1, 8, 2, 5, 4, 3, 7, 9]
print(arr)
bucketsort(arr)
print(arr)
