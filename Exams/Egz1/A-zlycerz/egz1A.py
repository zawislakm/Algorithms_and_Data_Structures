import math

from egz1Atesty import runtests
import queue

"""
Z kazdego zamku zaczyna wychodzic nowa krawedz o koszcie przejscia po zarabowaniu zamku + r

Dijkstra pamieta czy juz rabowała zamek czy nie.
Jezeli nie to probuje rabowac zamek lub nie rabuje zamku dalej
Jezeli tak to nie moze rabowac i idzie tylko po nowych krwaedziach
Wyniki to minimum z weight gdy zamek byl rabowany lub weight gdy zamek nie był rabowany minus zloto w ostatnim zamku
"""


def gold(G: list, V: list, s: int, t: int, r: int) -> float:
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    vetex = [len(i) for i in G]
    visited = [[False for _ in range(2)] for _ in range(n)]
    weight = [[math.inf for _ in range(2)] for _ in range(n)]
    weight[s] = [0, 0]

    for u in range(n):  # dodanie krawedzi które beda po zrabowaniu
        tmp = []
        for v, p in G[u]:
            tmp.append((v, 2 * p + r))
        G[u] += tmp

    Q = queue.PriorityQueue()
    Q.put((0, 0, s))  # waga, flaga czy mozna krasc, wierzcholek

    while not Q.empty():
        w, flag, u = Q.get()

        if flag == 0:  # jeczcze nie rabował
            for v, p in G[u][:vetex[u]]:
                # nie rabuje
                if weight[v][0] > w + p:
                    weight[v][0] = w + p
                    Q.put((w + p, 0, v))

            for v, p in G[u][vetex[u]:]:
                # rabuje
                if weight[v][1] > w + p - V[u]:
                    weight[v][1] = w + p - V[u]
                    Q.put((w + p - V[u], 1, v))

        if flag == 1:  # juz rabował
            for v, p in G[u][vetex[u]:]:
                if weight[v][1] > w + p:
                    weight[v][1] = w + p
                    Q.put((w + p, 1, v))

        visited[u][flag] = True

    # gdy dotralem bez rabowania to odjac zloto z zamku ostaniego
    print(weight[t])
    return min(weight[t][0] - V[t], weight[t][1])


G = [[(1, 9), (2, 2)],  # 0
     [(0, 9), (3, 2), (4, 6)],  # 1
     [(0, 2), (3, 7), (5, 1)],  # 2
     [(1, 2), (2, 7), (4, 2), (5, 3)],  # 3
     [(1, 6), (3, 2), (6, 1)],  # 4
     [(2, 1), (3, 3), (6, 8)],  # 5
     [(4, 1), (5, 8)]]  # 6
V = [25, 1000, 20, 15, 5, 10, 0]
s = 0
t = 6
r = 7
gold(G, V, s, t, r)

# zmien all_tests na True zeby uruchomic wszystkie testy
# runtests(gold, all_tests=True)


