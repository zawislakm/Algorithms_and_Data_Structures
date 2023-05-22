import math


# O(VE)


def BellmanFord(G: list, s: int):
    n = len(G)
    weights = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    weights[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                if weights[u] != math.inf and w + weights[u] < weights[v]:
                    parent[v] = u
                    weights[v] = w + weights[u]

    # looking for negative cycle

    for u in range(n):
        for v, w in G[u]:
            if weights[u] != math.inf and weights[v] > w + weights[u]:
                return None


    return weights



dijkstraGraphModyfied = [[(1, -3), (8, 1), (3, 3)], [(0, 3)], [(3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]
s = 8

BellmanFord(dijkstraGraphModyfied,s)
