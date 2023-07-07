"""
Sorted array of number. Find number x
Sum of all element |A[i]-x|
is minimal
"""

"""
Greedy
Is just median
"""

def distance(A: list) -> int:
    n = len(A)

    if n % 2 == 1:
        x = A[n // 2]
    else:
        x = round((A[n // 2] + A[n // 2 - 1]) / 2)

    return x


A = [1, 4, 6, 15, 100]
print(distance(A))
