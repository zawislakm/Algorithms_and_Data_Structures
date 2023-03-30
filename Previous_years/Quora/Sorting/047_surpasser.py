from typing import List, Tuple


def mergesort(A: List[Tuple[int, int]]) -> None:
    if len(A) < 2:
        return
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    mergesort(left)
    mergesort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        A[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        A[k] = right[j]
        j += 1
        k += 1


def surpasser(A: List[int]) -> List[int]:
    n = len(A)
    output = [0 for _ in range(n)]
    for i in range(n):
        A[i] = (A[i], i)
    mergesort(A)
    swap = 0
    for i in range(n):
        # quick math

        if A[i][1] > i:
            output[A[i][1]] = n - A[i][1] - 1
            swap += 1
        elif A[i][1] < i:
            output[A[i][1]] = n - i - 1
        else:
            output[A[i][1]] = (n - 1 * swap) - (swap * 2)

    return output


array = [6, 4, 3, 9, 7, 10]
array = [4, 6, 3, 9, 7, 10]
print(surpasser(array))
