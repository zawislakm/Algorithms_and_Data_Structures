"""
A set of points on a straight line is given. Please provide an algorithm that finds the minimal number of intervals
unit needed to cover all points of X
(Example: If X = {0.25,0.5,1.6} then two intervals are needed, e.g. [0.2,1.2] and [1.4,2.4])
"""

"""
Just greedy, creating new segment when previous is out of reach
"""


def segments(P: list) -> int:
    P.sort()
    used = [(P[0], P[0] + 1)]
    n = len(P)

    for i in range(1, n):

        if P[i] > used[-1][1]:
            used.append((P[i], P[i] + 1))

    return len(used)


points = [0.25, 0.5, 1.6, 1.7, 2.6]
segments(points)
