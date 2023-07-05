"""
There is given list of streets in city (edges) and list of buildings (factories or shops). The task is to check whether
is it possible to supply all shops with products from factories. 
"""

"""
Create graph with two extra vertices, s that is connected to each factory with flow equal to production of this factory
and t that all shops are connected with flow equal to demand, then use FordFulkerson algorythem and check whether max 
flow is equal to product demand of shops
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


inf = 10 ** 10


def industry(V: list, E: list) -> bool:
    # graf creation
    n = len(V) + 2
    G = [[0 for _ in range(n)] for _ in range(n)]

    for u, v in E:
        G[u][v] = inf

    s = n - 2  # start vertex
    t = n - 1  # end vertex
    demand = 0
    for i, (value, factory) in enumerate(V):
        if factory is True:
            G[s][i] = value
        else:
            demand += value
            G[i][t] = value
    # FordFulkerson logic
    return demand == FordFulkerson(G, s, t)


edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 5), (1, 6), (2, 4), (3, 4), (4, 5), (5, 6)]
# streets have no flow given, infinite flow possible there
vertices = [(7, True), (9, True), (3, True), (5, False), (8, False), (1, False), (4, False)]
# value produced/needed, True -> Factory, False -> Shop

print(industry(vertices, edges))
