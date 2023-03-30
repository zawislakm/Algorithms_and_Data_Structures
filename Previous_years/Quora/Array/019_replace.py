from typing import List


def replace(A: List[int]) -> None:
    n = len(A)

    left = [0 for _ in range(n)]
    right = [0 for _ in range(n)]

    left[0] = A[0]
    for i in range(1, n):
        left[i] = A[i] * left[i - 1]
    right[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        right[i] = A[i] * right[i + 1]

    A[0] = right[1]
    A[n - 1] = left[n - 2]
    for i in range(1, n - 1):
        A[i] = left[i - 1] * right[i + 1]


array = [5, 3, 4, 2, 6, 8]
print(array)
replace(array)
print(array)
