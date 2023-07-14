from egzP5btesty import runtests

time = 0


# szukanie puntkow artykulacji nlong
def articulation(G):
    def dfs(G, ART, LOW, D, P, v):
        global time
        children = 0

        time += 1
        LOW[v] = time
        D[v] = time

        for s in G[v]:
            if D[s] is None:
                children += 1
                dfs(G, ART, LOW, D, P, s)

                if LOW[s] >= D[v]:
                    ART[v] = True
                LOW[v] = min(LOW[v], LOW[s])
            else:
                LOW[v] = min(LOW[v], D[s])

        return children

    global time

    n = len(G)
    ART = [False for _ in range(n)]  # czy punkt jest punketem artykulacji
    LOW = [None for _ in range(n)]  # low z wykladu
    D = [None for _ in range(n)]  # czas, discovery time
    P = [None for _ in range(n)]  # parent

    for i in range(n):
        if D[i] is None:
            if dfs(G, ART, LOW, D, P, i) > 1:
                ART[i] = True
            else:
                ART[i] = False
    count = 0
    for i in ART:
        if i is True:
            count += 1
    return count


def koleje(B):
    ans = None
    newB = []
    n = 0
    for a, b in B:
        newB.append((min(a, b), max(a, b)))
        n = max(a, b, n)
    n += 1
    newB.sort(key=lambda x: (x[0], x[1]))
    B = newB

    G = [[] for _ in range(n)]
    prev = None
    for i in range(len(B)):
        if B[i] != prev:
            prev = B[i]
            a, b = B[i][0], B[i][1]
            G[a].append(b)
            G[b].append(a)

    ans = articulation(G)

    return ans


runtests(koleje, all_tests=True)

B = [
    (3, 1), (0, 1), (4, 2),
    (1, 2), (0, 1), (2, 4),
    (2, 4), (0, 3), (2, 4),
    (1, 0), (2, 1)
]
koleje(B)
