from zad9testy import runtests
import queue


def FordFulkerson(G: list, s: int, t: int) -> int:
    n = len(G)
    max_flow = 0

    parents = [-1 for _ in range(n)]

    def BFS() -> bool:
        nonlocal G, s, t, parents

        visited = [False for _ in range(n)]
        Q = queue.Queue()
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in range(n):
                if visited[v] is False and G[u][v] > 0:
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
            flow = min(flow, G[parents[pointer]][pointer])
            pointer = parents[pointer]
        max_flow += flow

        pointer = t
        while s != pointer:
            u = parents[pointer]
            G[u][pointer] -= flow
            G[pointer][u] += flow
            pointer = parents[pointer]

    # max_flow find amount of elements from s to t in this case 4 elements to 1 and 2 elements to 3 for example
    return max_flow


def creatGraphCopy(G) -> list:
    n = len(G)
    newG = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newG[i][j] = G[i][j]
    return newG


def maxflow(G, s):
    # tu prosze wpisac wlasna implementacje

    # Graph prepare
    n = 0
    for u, v, p in G:
        n = max(u, v, n)
    n += 1

    M = [[0 for _ in range(n)] for _ in range(n)]

    for u, v, p in G:
        M[u][v] = p

    max_flow_first = 0
    nextGraph = None
    for t in range(n):

        if t != s:
            tmpG = creatGraphCopy(M)
            flow_t = FordFulkerson(tmpG, s, t)
            if flow_t > max_flow_first:
                max_flow_first = flow_t
                nextGraph = creatGraphCopy(tmpG)

    max_flow_second = 0
    for t in range(n):
        if t != s:
            tmpG = creatGraphCopy(nextGraph)
            flow_t = FordFulkerson(tmpG, s, t)
            if flow_t > max_flow_second:
                max_flow_second = flow_t


    return max_flow_second+max_flow_first

    # zmien all_tests na True zeby uruchomic wszystkie testy


runtests( maxflow, all_tests = True )


G = [(0, 1, 7), (0, 3, 3), (1, 3, 4), (1, 4, 6), (2, 0, 9), (2, 3, 7), (2, 5, 9),
     (3, 4, 9), (3, 6, 2), (5, 3, 3), (5, 6, 4), (6, 4, 8)]
s = 2
print(maxflow(G, s))
