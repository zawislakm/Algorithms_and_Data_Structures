from typing import List, Tuple


def merge_sort(A: List[int]) -> None:
    if len(A) < 2:
        return
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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


def find_pair(A: List[int], target: int) -> Tuple[int, int]:
    merge_sort(A)
    i = 0
    j = len(A) - 1
    while i != j:
        if A[i] + A[j] == target:
            return A[i],A[j]
        if A[i] + A[j] < target:
            i += 1
        else:
            j -= 1

    return -1, -1


nums = [8, 7, 2, 5, 3, 1]
target = 10
print(find_pair(nums,target))
nums = [5, 2, 6, 8, 1, 9]
target = 12
print(find_pair(nums,target))