"""
There is given graph with vertices s and t, find number of paths that uses uniq vertices
(each vertex can be used only once)
"""

"""
Divide all vertices to 2 vertex, first should have incoming edges and second only outgoing edges. First and second
vertex should be connected only with one edge. Use FordFulkerson algorythem to find max flow which will be equal
to amount of uniq paths
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


def paths(E: list, s: int, t: int, n: int) -> int:
    pass

    G = [[0 for _ in range(2 * n)] for _ in range(2 * n)]

    for u, v in E:
        G[u+n][v] = 1

    for u in range(n):
        G[u][u + n] = 1

    G[s][s + n] = INF

    return FordFulkerson(G, s, t)


edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2,5),(2, 6), (3, 6), (4, 8), (5, 8), (5, 4), (6, 5), (6, 7), (7, 8)]
# remove (2,5) to lower number of paths
vertices = 9
print(f"Found amount of paths: {paths(edges, 0, 8, vertices)}")

