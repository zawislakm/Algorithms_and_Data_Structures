"""
Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych w acyklicznym grafie skierowanym?
"""

"""
ustawic topologicznie wierzcholki, nastepnie startujac wiercholka s do konca ustawinie tologiczinego
ustawiac najlepsze dystnse dostania sie 
"""


from math import inf




def paths(G: list, s: int) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [inf for _ in range(n)]
    distance[s] = 0
    topology = []

    def dfs_visit(u: int) -> None:
        nonlocal G, visited, topology
        visited[u] = True
        for v, _ in G[u]:
            if visited[v] is False:
                dfs_visit(v)
        topology.append(u)

    for u in range(n):
        if visited[u] is False:
            dfs_visit(u)
    topology.reverse()

    ind = topology.index(s)

    for u in range(ind, n):
        for v, p in G[u]:
            if distance[v] > distance[u] + p:
                distance[v] = distance[u] + p

    return distance


graph = [[(1, 3), (2, 6)],
         [(2, 2), (3, 1), (5, 8)],
         [(4, 7), (3, 5)],
         [(5, 2), (4, 5)],
         [(5, 3)],
         []]
print(paths(graph, 0))
