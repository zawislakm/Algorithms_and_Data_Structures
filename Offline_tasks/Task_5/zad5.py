import math
from zad5testy import runtests
from queue import PriorityQueue

"""
Simple add vertice between peculiarities and Dijkstra Algorithm
"""


def spacetravel(n: int, E: list, S: list, a: int, b: int) -> int:
    G = [[] for _ in range(n + 1)]
    for u, v, w in E:  # m
        G[u].append((v, w))
        G[v].append((u, w))

    for u in S:
        G[u].append((n, 0))
        G[n].append((u, 0))
    n += 1
    visited = [False for _ in range(n)]
    weights = [math.inf for _ in range(n)]

    weights[a] = 0
    Q = PriorityQueue()
    Q.put((0, a))

    while not Q.empty():
        w, u = Q.get()
        if visited[u] is False:
            for v, p in G[u]:
                if visited[v] is False and weights[v] > w + p:
                    weights[v] = w + p
                    Q.put((w + p, v))
            visited[u] = True

    if weights[b] == math.inf:
        return None

    return weights[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
