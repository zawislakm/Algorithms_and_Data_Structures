"""
Trailer with a capacity of K kilograms and set of weights. The weight of each load is a power of two
(for example, for seven loads the weights can be 2,2,4,8,1,8,16 and the capacity K=27). Select the loads so that
the trailer is as full as possible, and at the same time use as few loads as possible.
(its better to use 100 loads to K capacity than one load to capacity K-1)
"""

"""
Greedy
Using the information that values of the charges are the values of powers of the same base (works not only for 2).
Just sort in descending order and take the values that fit.
"""


def pack(P: list, K: int) -> list:
    P.sort(reverse=True)
    items = []

    for i in P:
        if K - i >= 0:
            K -= i
            items.append(i)

    print(f'Used items {items}')
    return items


packages = [2, 2, 4, 8, 1, 8, 16]
K = 27
pack(packages,K)
