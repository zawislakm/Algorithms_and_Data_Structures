
from zad1testy import runtests



def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [False for _ in range(n)]
    petrol = [0 for _ in range(n)]
    weights = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    weights[a] = 0
    # visited[a] = True
    petrol[a] = d
    for _ in range(n):

        u = -1
        lowest = float('inf')
        for v in range(n):
            if visited[v] is False and weights[v] < lowest:
                lowest = weights[v]
                u = v
        oil = petrol[u]
        if u in P:
            oil = d
        # check whether weight of node is to big or petrol incoming willbe better
        for v in range(n):
            if visited[v] is False and (weights[v] > weights[u] + G[u][v] or petrol[v] < oil - G[u][v])and G[u][v] <= oil and G[u][v] > 0:
                petrol[v] = oil - G[u][v]
                parent[v] = u
                weights[v] = weights[u] + G[u][v]

        visited[u] = True

    if weights[b] == float('inf'):
        return None

    path = [b]
    while b != a:
        b = parent[b]
        path.append(b)
    path.reverse()
    print(f"Path: {path}")
    return path

        

runtests( jak_dojade ) 
