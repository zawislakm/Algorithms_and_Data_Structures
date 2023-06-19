from zad2testy import runtests

from math import ceil, sqrt


def find_distance(A1, A2):
    x1, y1 = A1
    x2, y2 = A2
    return ceil(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def Kruskal(G: list, n: int) -> int:
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]

    def find(x: int) -> int:
        if parent[x] != x:
            x = find(parent[x])
        return x

    def union(x: int, y: int) -> None:
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

    max_e = -1
    min_e = float('inf')
    i = e = 0

    while e < n - 1:
        u, v, w = G[i]
        i += 1
        if find(u) != find(v):
            union(u, v)
            max_e = max(max_e, w)
            min_e = min(min_e, w)
            e += 1
        if i == len(G):
            return float('inf')
    return max_e - min_e


def highway(A):
    # tu prosze wpisac wlasna implementacje

    # Graph prepare
    G = []
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            G.append((i, j, find_distance(A[i], A[j])))

    # Kruskal len(G) times, deleting always lowest cost edge
    G.sort(key=lambda x: x[2])
    return_value = 10 ** 10
    ans = float('inf')
    while G != [] and return_value != float('inf'):
        return_value = Kruskal(G, n)
        ans = min(ans, return_value)
        del G[0]

    return ans
        

runtests( highway ) 
