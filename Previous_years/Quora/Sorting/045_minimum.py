import sys


def minimum(A: list) -> int:
    min1 = sys.maxsize
    min2 = sys.maxsize
    min3 = sys.maxsize
    max2 = -sys.maxsize
    max1 = -sys.maxsize

    def pick_min(num: int):
        nonlocal min1, min2, min3
        if min1 > num:
            min1, num = num, min1
        if min2 > num:
            min2, num = num, min2
        if min3 > num:
            min3 = num

    def pick_max(num: int):
        nonlocal max1, max2
        if num > max1:
            max1, num = num, max1
        if num > max2:
            max2 = num

    for x in A:
        pick_max(x)
        pick_min(x)

    return min(max1 * max2 * min1, min1 * min2 * min3)


array = [3, 4, 1, 2, 5]
print(minimum(array))
