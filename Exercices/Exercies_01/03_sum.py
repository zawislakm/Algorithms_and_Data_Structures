"""
In sorted array, find indexes of elements whose sum equals given target
"""

"""
Start is pointer to first element (position 0), end is pointer to last element( position array length -1), 
they both move inside array, 
Depending on the difference between target and sum of arr[start] + arr[end]:
smaller -> start pointer increase, 
bigger -> end pointer decrease,
if pointers meet it means it is impossible to reach given target

Test cases:
[1, 3, 5, 8, 11, 20]
target = 25 -> 5 + 20 (2,5)
target = 27 -> impossible 
target = 13 -> 5 + 8 (2,3)
target = 15 -> impossible
"""
# n
from typing import List, Tuple


def find_sum(arr: List[int], target: int) -> Tuple[int, int]:
    n = len(arr)
    start = 0
    end = n - 1

    while True:

        if start == end:
            break
        if target == arr[start] + arr[end]:
            return start, end
        if target > arr[start] + arr[end]:
            start += 1
        else:
            end -= 1
    return -1, -1


arr = [1, 3, 5, 8, 11, 20]
target_0 = 25
target_1 = 27
target_2 = 13
target_3 = 15


print(find_sum(arr,target_0))
