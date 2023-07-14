import math
import queue

from egzP1btesty import runtests


def turysta(G: list, D: int, L: int) -> int:
    # tutaj proszę wpisać własną implementację
    n = 0
    for u, v, _ in G:
        n = max(u, v, n)

    n += 1

    H = [[] for _ in range(n)]
    for u, v, p in G:
        H[u].append((v, p))
        H[v].append((u, p))
    G = H

    # for i,j in enumerate(G):
    #     print(i,j)

    weight = [[math.inf for _ in range(5)] for _ in range(n)]
    visited = [[False for _ in range(5)] for _ in range(n)]
    weight[D][0] = 0
    Q = queue.PriorityQueue()
    Q.put((0, 1, D))

    while not Q.empty():
        w, ind, u = Q.get()
        if ind < 5:
            for v, p in G[u]:
                if visited[v][ind] is False and weight[v][ind] > w + p:
                    weight[v][ind] = w + p
                    Q.put((w + p, ind + 1, v))
            visited[u][ind - 1] = True

    return weight[L][4]


runtests(turysta)

G = [
    (0, 1, 9), (0, 2, 1),
    (1, 2, 2), (1, 3, 8),
    (1, 4, 3), (2, 4, 7),
    (2, 5, 1), (3, 4, 7),
    (4, 5, 6), (3, 6, 8),
    (4, 6, 1), (5, 6, 1)
]
D = 0
L = 6
turysta(G, D, L)
