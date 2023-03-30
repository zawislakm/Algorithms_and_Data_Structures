from typing import List


def move(A: List[int]) -> None:
    n = len(A)
    k = 0

    for i in range(n):
        if A[i] != 0:
            A[k] = A[i]
            k += 1
    for i in range(k, n):
        A[i] = 0


def move2(A: List[int]) -> None:
    n = len(A)
    j = 0
    for i in range(n):
        if A[i] != 0:
            A[i], A[j] = A[j], A[i]
            j += 1


array = [6, 0, 8, 2, 3, 0, 4, 0, 1]
print(array)
move2(array)
print(array)
