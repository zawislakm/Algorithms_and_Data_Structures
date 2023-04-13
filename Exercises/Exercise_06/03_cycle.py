"""
Check whether exists cycle of length 4 in undirected graph
"""

"""
Check whether 2 vertex have 2 same neighbours
"""
from Graph import GraphTransformations as t


def checkCycle(G: list) -> bool:
    n = len(G)
    G = t.list_to_matrix(G)

    def check(u, v) -> bool:
        count = 0
        for a in range(n):
            if G[u][a] == 1 and G[v][a] == 1:
                count += 1
            if count == 2:
                return True
        return False

    for u in range(n):
        for v in range(u + 1, n):
            if check(u, v):
                return True
    return False


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12],
               [9, 12],
               [10, 11]]

simpleGraphAdd = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3], [4, 8], [5, 7, 9], [8, 10], [9, 12],
               [ 12],
               [10, 11]] #egde between 8 and 6 deleted; 9 and 11 deleted

print(checkCycle(simpleGraph))
print(checkCycle(simpleGraphAdd))
