# Przewodnik chce przewieźć grupę K turystów z miasta A do miasta B. Po drodze jest jednak wiele innych
# miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. Mamy daną listę trójek postaci
# (x, y, c), gdzie x i y to miasta między którymi bezpośrednio jeździ autobus o pojemności c pasażerów.
# Przewodnik musi wyznaczyć wspólną trasę dla wszystkich turystów i musi ich podzielić na grupki tak, żeby
# każda grupka mogła przebyć trasę bez rozdzielania się. Proszę podać algorytm, który oblicza na ile
# (najmniej) grupek przewodnik musi podzielić turystów (i jaką trasą powinni się poruszać), żeby wszyscy
# dostali się z A do B.

"""
Modified dijkstra, remembering the maximum weight of the edge that came to it
"""

import math
import queue


def tourists(E: list, s: int, t: int, n: int, c: int) -> (int, list):
    G = [[] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]
    max_edge = 0
    for u, v, p in E:
        G[u].append((v, p))
        G[v].append((u, p))
        M[u][v] = M[v][u] = p
        max_edge = max(max_edge, p)

    visited = [False for _ in range(n)]
    weight = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = queue.PriorityQueue()
    Q.put((max_edge + 1, s))
    weight[s] = max_edge + 1

    while not Q.empty():
        distance, u = Q.get()
        for v, p in G[u]:
            real_distance = min(weight[u], p)
            if visited[v] is False and real_distance > weight[v]:
                weight[v] = real_distance
                parent[v] = u
                Q.put((max_edge - weight[v], v))
        visited[u] = True

    path = [t]
    min_edge = max_edge + 1
    prev = t
    pointer = parent[prev]
    while pointer is not None:
        min_edge = min(min_edge, M[prev][pointer])
        path.append(pointer)
        prev, pointer = pointer, parent[pointer]

    group_amounts = math.ceil(c / min_edge)

    print(f'Found path is {path}, tourists need to be decided into {group_amounts} groups')

    return group_amounts, path


graph = [(0, 1, 12), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14),
         (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]
city_a = 0
city_b = 7
tourists(graph, city_a, city_b, 8, 20)
