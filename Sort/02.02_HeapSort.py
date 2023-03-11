from typing import List


# nlogn

def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def parent(i: int) -> int:
    return (i - 1) // 2


def swap(arr: List[int], i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def heapify(arr: List[int], i: int, n: int) -> None:
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and arr[l] > arr[max_index]: max_index = l
    if r < n and arr[r] > arr[max_index]: max_index = r

    if max_index != i:
        swap(arr, i, max_index)
        heapify(arr, max_index, n)


def buildheap(arr: List[int]) -> None:
    n = len(arr)
    for i in range(parent(n - 1), -1, -1):
        heapify(arr, i, n)


def heapsort(arr: List[int]) -> None:
    n = len(arr)
    buildheap(arr)
    for i in range(n - 1, 0, 1):
        swap(arr, 0, i)
        heapify(arr, 0, i)
    arr.reverse()


arr = [1, 8, 2, 5, 4, 3, 7, 9]
print(arr)
heapsort(arr)
print(arr)
