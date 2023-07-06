"""
Recreate path in graph
"""
from Graph import GraphTransformations as GT

INF = 10 * 10


def Dijkstra(G: list, s: int, t: int) -> list:
    global INF
    G = GT.list_to_matrix_wages(G)
    n = len(G)
    visited = [False for _ in range(n)]
    weights = [INF for _ in range(n)]
    parents = [None for _ in range(n)]
    weights[s] = 0

    for _ in range(n):

        best = index = 1000

        for u in range(n):
            if weights[u] < best and visited[u] is False:
                best = weights[u]
                index = u

        u = index
        for v in range(n):
            if G[u][v] != 0 and weights[v] > weights[u] + G[u][v] and visited[v] is False:
                weights[v] = weights[u] + G[u][v]
                parents[v] = u

        visited[u] = True

    print(weights)

    if visited[t]:
        path = []
        while t != None:
            path.append(t)
            t = parents[t]
        path.reverse()
        print(f'Found path is {path}, with cost of {weights[path[-1]]}')
        return path

    return None


dijkstraGraph = [[(1, 3), (8, 1), (3, 3)], [(0, 3), (2, 5)], [(1, 5), (3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]

Dijkstra(dijkstraGraph, 0, 5)
