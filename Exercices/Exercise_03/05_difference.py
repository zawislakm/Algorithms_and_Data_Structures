"""
In liner way with given array A find numbers (x,y), where y-x is maximum and x and y would be next to each other after
sorting this array
"""
"""
Solution requires using bucket sort idea, then compering max element from bucket on index i and minimum element from 
first not empty bucket on index j (i < j) 
"""
from typing import List


def find_difference(A: List[float]) -> (float, float):
    n = len(A)
    buckets = [[] for _ in range(n + 1)]

    # max_e = max(A)
    # min_e = min(A)

    for x in A:
        # index = int((x - min_e) / (max_e - min_e))
        index = int(x * n)
        buckets[index].append(x)

    y = -1
    x = -1

    for i in range(0, n):
        if buckets[i]:  # not empty
            j = i + 1

            while not buckets[j]:  # find first not empty on right
                j += 1
                if j == n + 1:
                    break
            else:
                if min(buckets[j]) - max(buckets[i]) > y - x:
                    y = min(buckets[j])
                    x = max(buckets[i])

    print(buckets)
    return y, x


arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(find_difference(arr))
