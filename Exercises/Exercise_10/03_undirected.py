"""
Find max flow in undirected graph
"""

"""
To find max flow in undirected graph each edge need to be split in two with one extra 
vertex with new four directed edges. Than FordFulkerson algorythem easily can find max flow.
"""

import queue


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
        path = [t]
        flow = float('inf')
        pointer = t
        while s != pointer:
            flow = min(G[parents[pointer]][pointer], flow)
            pointer = parents[pointer]
            path.append(pointer)
        print(path[::-1],flow)
        max_flow += flow

        pointer = t
        while s != pointer:
            u = parents[pointer]
            G[u][pointer] -= flow
            G[pointer][u] += flow
            pointer = u
    return max_flow


def undirected_flow(E: list, n: int, s: int, t: int) -> int:
    # len(E) edges amount, n vertices amount
    # creating directed graph from undirected
    G = [[0 for _ in range(n + len(E))] for _ in range(n + len(E))]

    for i, (u, v, w) in enumerate(E):
        G[u][i + n] = w
        G[i + n][u] = w
        G[v][i + n] = w
        G[i + n][v] = w

    return FordFulkerson(G, s, t)


edges = [(0, 1, 8), (0, 2, 5), (1, 3, 4), (2, 3, 7), (3, 4, 9), (2, 4, 11)]
vertices = 5
print(undirected_flow(edges, vertices, 0, 4))
