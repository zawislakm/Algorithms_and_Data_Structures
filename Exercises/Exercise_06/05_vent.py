"""
In directed graph find whether exists vertex that is not connected to other vertexes and  all other vertexes are 
connected to it
"""

"""
Using matrix graph representation find vertex where row is only 0 values and column only 1 values
"""
from Graph import GraphTransformations as t


def vent(G: list) -> bool:
    G = t.list_to_matrix(G)
    n = len(G)

    for u in range(n):

        for v in range(n):
            if G[u][v] != 0:
                break
            if G[v][u] != 1 and v != u:
                break
        else:
            return True
    return False


G = [[1, 2], [2, 4], [], [2], [2, 3]]
print(vent(G))
