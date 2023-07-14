from egzP3btesty import runtests
from queue import PriorityQueue

"""
Maksymalne drzweo rozpinajace plus jedna dodaktowa krawedz jest szukana

Graf jest zamieniany na liste krawedzi E. Stare koszty krwaedzi sa zapamietywane, dopisywany jest nowy koszt rowny
maksymalan waga krawedzi - prawdziwa waga krawedzi. Sortowane sa po nowej wadze i odpalny jest algorytm Kruskala.
W sumowaniu wag dla MST w kruskalu sumowane sa oryginalne wagi krawedzi oraz zapamitywane sa krawedzi które zostały
użyte. Dodawan jest pierwsza nieuzytwa krawedzi do wyniki kruskala. Wynikiem jest suma wszystki krawedzi - wynik Kruskala
"""

def Kruskal(G: list, n: int):
    parent = [x for x in range(n)]
    rank = [0 for _ in range(n)]
    used = [False for _ in range(len(G))]

    def find(x):
        if x != parent[x]:
            return find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    i = e = w = 0

    while e < n - 1:
        u, v, p, _ = G[i]
        i += 1

        if find(u) != find(v):
            e += 1
            used[i - 1] = True
            w += p
            union(u, v)

    f = 0
    while used[f] is True:
        f += 1

    w += G[f][2]

    return w


def lufthansa(G: int):
    # tutaj proszę wpisać własną implementację
    n = len(G)
    E = []
    max_edge = 0
    all_edges = 0
    for u, e in enumerate(G):
        for v, p in e:
            if u < v:
                max_edge = max(max_edge, p)
                all_edges += p
                E.append([u, v, p, 0])

    for i, (_, _, p, _) in enumerate(E):
        E[i][3] = max_edge - p

    E.sort(key=lambda x: x[3])
    result = Kruskal(E, n)

    return all_edges - result


runtests(lufthansa, all_tests=True)

G = [
    [(1, 15), (2, 5), (3, 10)],
    [(0, 15), (2, 8), (4, 5), (5, 12)],
    [(0, 5), (1, 8), (3, 5), (4, 6)],
    [(0, 10), (2, 5), (4, 2), (5, 11)],
    [(1, 5), (2, 6), (3, 2), (5, 2)],
    [(1, 12), (4, 2), (3, 11)]
]
lufthansa(G)
