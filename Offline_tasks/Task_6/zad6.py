from zad6testy import runtests

"""
Maximum matching solution found with FordFulkerson using DFS on list graph
"""

def binworker(M:list) -> int:
    # graph prepare
    m = len(M)
    n = 2 * m + 2
    s = 2 * m
    t = s + 1
    G = [[] for _ in range(n)]
    for u in range(m):
        for v in M[u]:
            G[u].append(v + m)
        G[s].append(u)
        G[u + m].append(t)

    # FordFulkerson logic
    parent = [None for _ in range(n)]

    def DFS():
        visited = [False for _ in range(n)]
        stack = []
        stack.append(s)
        visited[s] = True

        while stack:
            u = stack.pop()
            for v in G[u]:
                if visited[v] is False:
                    visited[v] = True
                    stack.append(v)
                    parent[v] = u
                    if v == t:
                        return True
        return False

    flow = 0
    while DFS():
        pointer = t
        while pointer != s:
            next_pointer = parent[pointer]
            G[next_pointer].remove(pointer)
            G[pointer].append(next_pointer)
            pointer = next_pointer

        flow += 1

    return flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(binworker, all_tests=False)

