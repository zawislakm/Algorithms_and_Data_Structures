from zad8testy import runtests
from queue import PriorityQueue

"""
Greedy oil
"""


def plan(T: list) -> int:
    n = len(T)
    m = len(T[0])
    oil_array = [0 for _ in range(m)]

    def oil_collector(u: int, v: int, index: int) -> None:
        nonlocal T, oil_collector, n, n
        if T[u][v] != 0:
            oil_array[index] += T[u][v]
            T[u][v] = 0
            for i, j in [(u - 1, v), (u + 1, v), (u, v - 1), (u, v + 1)]:
                if 0 <= i < n and 0 <= j < m:
                    oil_collector(i, j, index)

    for i in range(m):
        oil_collector(0, i, i)

    stops = oil = i = 0
    Q = PriorityQueue()
    while oil + 1 < m:
        while i <= oil:
            if oil_array[i] != 0:
                Q.put(-1 * oil_array[i])
            i += 1
        oil += Q.get() * -1
        stops += 1

    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
