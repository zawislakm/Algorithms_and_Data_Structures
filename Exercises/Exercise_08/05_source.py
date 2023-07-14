"""
Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek można
osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który stwierdza czy dany graf
zawiera dobry początek.
"""

"""
Normal DFS, with memorization of processing time. 
Than visited array is reset. Find vertex where processing time is equal to amount of vertices. Run DFS only from this
vertex. Check whether is possible to reach all other vertices
"""


import math



from math import inf


def good_start(G: list) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    times = [inf for _ in range(n)]

    time = 0

    def DFS_visit(u: int):
        nonlocal G, visited, times, time
        visited[u] = True
        for v in G[u]:
            if visited[v] is False:
                DFS_visit(v)
        time += 1
        times[u] = time

    for t in range(n):
        if visited[t] is False:
            DFS_visit(t)

    visited = [False for _ in range(n)]

    for u,t in enumerate(times):
        if t == n:
            DFS_visit(u)
            if False in visited:
                return False
            else:
                return u
    return False


graph = [[4],
         [2],
         [0, 3], #remove 3 to False
         [1],
         []]
print(good_start(graph))
