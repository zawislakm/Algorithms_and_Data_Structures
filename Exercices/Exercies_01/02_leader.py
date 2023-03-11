"""
Leader problem: leader is a value that appears more than on half positions in array, 
check if there is leader in the array
"""

"""
Type first element (position 0) as our leader and set count to 1, in loop throughout array when element equals to typed
leader count is increased, otherwise is decreased, when the count is below 0 current elements become our new typed leader
Typed leader needs to be checked whether it appears on half positions in array

Test cases:
[1, 3, 5, 7, 5, 4, 6, 8, 9, 2, 4, 1, 5, 7, 3] #False
[3, 5, 2, 1, 5, 3, 5, 4, 5, 5, 6, 5, 5, 5, 5] #True, leader: 5
"""
# n
from typing import List


def find_leader(arr: List[int]) -> bool:
    n = len(arr)
    leader = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] == leader:
            count += 1
        else:
            count -= 1
        if count < 0:
            leader = arr[i]

    check = 0
    for num in arr:
        if num == leader:
            check += 1

    return n // 2 < check


test_0 = [3, 5, 2, 1, 5, 3, 5, 4, 5, 5, 6, 5, 5, 5, 5]
test_1 = [1, 3, 5, 7, 5, 4, 6, 8, 9, 2, 4, 1, 5, 7, 3]
print(find_leader(test_1))
