from kol2testy import runtests

"""
Graph is converted to list of edges (E), then Kruskal algorithm  looks for beautiful tree (n-1 edges), if algorithm 
skips any edges work is being interrupted, cuz it needs to be next n-1 edges

O(VElog*E)


O(VE) solution
Sort list of edges by their cost, check first n-1 edges whether is MST with BFS or DFS if not remove 0 edge and next 
edges from list till finding max MST
"""


def Kruskal(G, n):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parent[x] != x:
            x = find(parent[x])
        return x

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

    i = e = 0
    total_weight = 0
    while e < n - 1:
        u, v, w = G[i]
        i += 1
        if find(u) != find(v):
            union(u, v)
            e += 1
            total_weight += w

        else:
            # skipping edge means stopping algorythem
            return -1
        if i == len(G):
            return -1,

    return total_weight


def beautree(G):
    n = len(G)
    E = []

    for u in range(n):
        for v, w in G[u]:
            if u < v:
                E.append((u, v, w))

    E.sort(key=lambda x: x[2])

    while len(E) > n - 1:
        total_weight = Kruskal(E, n)
        if total_weight != -1:
            return total_weight
        del [E[0]]

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
