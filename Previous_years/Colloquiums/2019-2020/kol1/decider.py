from typing import List

"""
Arrays needs to be sorted, than loop goes through elements and find sums from them, remembering index , not to use the
now looked number to sum (1+0 = 1)

arr = [-1, -1, 0, 1, 1, 2]
index = 0, value -1, sum = -1(index 1) + 0(index2)
index = 1, value -1, sum = -1(index 0) + 0(index2)
index = 2, value  0, sum = -1(index 1) + 1(index3)
index = 3, value  1, sum =  1(index 4) + 0(index2)
index = 4, value  1, sum =  1(index 3) + 0(index2)
index = 5, value  2, sum =  1(index 3) + 1(index4)
"""


def find_sum(arr: List[int], target: int, index: int) -> bool:
    n = len(arr)
    start = 0
    end = n - 1

    while True:
        if start == end:
            break
        if start == index:
            start += 1
        if end == index:
            end -= 1
        if target == arr[start] + arr[end]:
            return True
        if target > arr[start] + arr[end]:
            start += 1
        else:
            end -= 1
    return False


def swap(A: List[int], i: int, j: int) -> None:
    A[i], A[j] = A[j], A[i]


def quicksort(A: List[int], p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


def decider(T: List[int]) -> bool:
    n = len(T)
    quicksort(T)

    for i in range(n):

        if not find_sum(T, T[i], i):
            return False

    return True


# arr = [2, 1, 1, 3, 5, 7, 9, 4, 13, 17, 16]
arr = [-1, -1, 0, 1, 1, 2]  # True
print(decider(arr))
