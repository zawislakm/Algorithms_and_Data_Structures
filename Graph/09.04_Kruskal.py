import GraphTransformations as GT


# O(ElogV)
# if weights are <0, just add the lowest value to all and solve MST (mst has always v-1 edges)

def Kruskal(G: list) -> int:
    n = len(G)
    G = GT.list_to_edge_list(G)
    print(G)
    G.sort(key=lambda x: x[2])

    def find(x: int) -> int:
        if parent[x] != x:
            x = find(parent[x])
        return x

    def union(x: int, y: int):
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

    parent = [v for v in range(n)]
    rank = [0 for _ in range(n)]

    i = e = 0
    total_weight = 0
    while e < n - 1:
        u, v, p = G[i]
        i += 1
        if find(u) != find(v):
            e += 1
            total_weight += p
            union(u, v)

    print("Parent: ", parent)
    print("Total MST weight: ", total_weight)
    return total_weight


mstGraph = [[(1, 1), (4, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 2), (4, 4), (3, 6)], [(2, 6), (4, 2)],
            [(0, 4), (2, 4), (3, 2), (5, 7)], [(0, 8), (4, 7)]]
Kruskal(mstGraph)
