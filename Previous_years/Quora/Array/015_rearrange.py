from typing import List


def rearrange(A: List[int]) -> None:
    n = len(A)
    for i in range(1, n - 1):
        if A[i - 1] > A[i] and i % 2 == 1:
            A[i - 1], A[i] = A[i], A[i - 1]

        if i % 2 == 1 and A[i + 1] > A[i]:
            A[i], A[i + 1] = A[i + 1], A[i]


array = [1, 2, 3, 4, 5, 6, 7]
array = [9, 6, 8, 3, 7]
array = [6, 9, 2, 5, 1, 4]
print(array)
rearrange(array)
print(array)
