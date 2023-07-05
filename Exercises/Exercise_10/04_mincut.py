"""
Mincut is equal to minimal maximal flow of graph

From undirected graph make graph directed, then pick one vertex as source and check max flow with all other vertices
Minimal of them is mincut and answer
"""


import queue
from copy import deepcopy


def FordFulkerson(G: list, s: int, t: int) -> int:
    n = len(G)
    parents = [-1 for _ in range(n)]

    def BFS() -> bool:
        nonlocal G, s, t, parents

        visited = [False for _ in range(n)]
        Q = queue.Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in range(n):
                if visited[v] is False and G[u][v] > 0:
                    Q.put(v)
                    visited[v] = True
                    parents[v] = u
                    if v == t:
                        return True
        return False

    max_flow = 0

    while BFS():
        flow = float('inf')
        pointer = t
        while s != pointer:
            flow = min(G[parents[pointer]][pointer], flow)
            pointer = parents[pointer]
        max_flow += flow

        pointer = t
        while s != pointer:
            u = parents[pointer]
            G[u][pointer] -= flow
            G[pointer][u] += flow
            pointer = u
    return max_flow


INF = 10 ** 10


def edges_consistency(E: list, n: int) -> int:
    # creating directed graph from undirected
    G = [[0 for _ in range(n + len(E))] for _ in range(n + len(E))]
    for i, (u, v) in enumerate(E):
        G[u][i + n] = 1
        G[i + n][u] = 1
        G[v][i + n] = 1
        G[i + n][v] = 1

    min_of_max_flows = INF

    for u in range(1, n):
        graph_copy = deepcopy(G)
        result = FordFulkerson(graph_copy, 0, u)
        min_of_max_flows = min(min_of_max_flows, result)

    return min_of_max_flows


edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (2, 6), (3, 6), (4, 8), (5, 8), (5, 4), (6, 5), (6, 7),
         (7, 8), ]
vertices = 9
edges_consistency(edges, vertices)
