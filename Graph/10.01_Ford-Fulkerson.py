import GraphTransformations as GT
import queue


# O(VE^2)

def FordFulkerson(G: list, s: int, t: int) -> int:
    n = len(G)
    M = GT.list_to_matrix_wages(G)
    max_flow = 0

    parents = [-1 for _ in range(n)]

    def BFS() -> bool:
        nonlocal M, s, t, parents

        visited = [False for _ in range(n)]
        Q = queue.Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in range(n):
                if visited[v] is False and M[u][v] > 0:
                    Q.put(v)
                    visited[v] = True
                    parents[v] = u
                    if v == t:
                        return True
        return False

    while BFS():

        flow = float('inf')
        pointer = t
        while s != pointer:
            flow = min(flow, M[parents[pointer]][pointer])
            pointer = parents[pointer]
        max_flow += flow

        pointer = t
        while s != pointer:
            u = parents[pointer]
            M[u][pointer] -= flow
            M[pointer][u] += flow
            pointer = parents[pointer]

    # max_flow find amount of elements from s to t in this case 4 elements to 1 and 2 elements to 3 for example
    return max_flow


flowGraph = [[(1, 4), (3, 3)], [(2, 2), (3, 2)], [(5, 4)], [(2, 2), (4, 2)], [(5, 5)], []]
s = 0
t = 5

print(FordFulkerson(flowGraph, s, t))
