"""
There is a graph as a map of cities. Two drivers, Alice and Bob. Alice want to drive as little as possible.
Driver change in each city. Alice plans the path and pick who drive first. Algorythem should find path
and who drive first
"""
"""
Trzeba odpalic dwa razy dijkestre, raz gdy startuje Alice raz gdy Bob, odpowienie warunki przy relaxowniu.

"""

from math import inf
from queue import PriorityQueue


def Dijkstra(G: list, weight: list, first: int, s: int, t: int) -> (int, list):
    n = len(G)
    Q = PriorityQueue()
    weight[0] = [0, 0]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    Q.put((0, first, s))

    def relax(v: int, u: int, now: int, next: int, p: int) -> bool:
        nonlocal weight, parent

        if weight[v][now] > weight[u][now] + p and now == 0:
            weight[v] = [weight[u][now] + p, weight[u][next]]
            return True
        elif now == 1:
            weight[v] = [weight[u][next], weight[u][now] + p]
            return True

        return False

    while not Q.empty():
        distance, new_person, u = Q.get()

        for v, p in G[u]:
            if not visited[v]:
                next_person = 1 - new_person

                if relax(v, u, new_person, next_person, p):
                    Q.put((weight[v][0], next_person, v))
                    parent[v] = u
        visited[u] = True

    return weight[t][0], parent


def planner(G: list, s: int, t: int) -> (bool, list):
    weight = [[inf for _ in range(2)] for _ in range(len(G))]
    # 0 - Alice, 1 - Bob
    result_1, parent_1 = Dijkstra(G, weight, 0, s, t)

    weight = [[inf for _ in range(2)] for _ in range(len(G))]
    result_2, parent_2 = Dijkstra(G, weight, 1, s, t)

    tour = []

    if result_1 < result_2:
        while t != parent_1[s]:
            tour.append(t)
            t = parent_1[t]
        tour.reverse()
        return True, tour
    else:
        while t != parent_2[s]:
            tour.append(t)
            t = parent_2[t]
        tour.reverse()
        return False, tour


graph = [[(1, 4), (2, 1), (3, 5)],
         [(0, 1), (4, 2)],
         [(0, 1), (5, 8), (6, 7)],
         [(0, 5), (5, 7)],
         [(1, 2), (7, 10)],
         [(2, 8), (3, 7), (8, 3)],
         [(2, 7), (7, 6)],
         [(4, 10), (6, 6), (9, 11)],
         [(5, 3), (9, 9)],
         [(7, 11), (8, 9)]]

start = 0
finish = len(graph) - 1
print(planner(graph, start, finish))
