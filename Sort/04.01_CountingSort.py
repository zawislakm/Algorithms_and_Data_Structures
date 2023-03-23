from typing import List


# n + k
# only on known range e.g [0,k-1]
# stable
def countingsort(A: List[int], k: int) -> None:
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for x in A:
        C[x] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    for i in range(n):
        A[i] = B[i]


arr = [2, 0, 3, 1, 1, 2, 3, 2]
print(arr)
countingsort(arr, max(arr) + 1)
print(arr)
