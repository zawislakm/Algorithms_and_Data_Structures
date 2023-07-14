from zad4testy import runtests


def select_buildings(T, p):
    # tu prosze wpisac wlasna implementacje

    X = []

    def prev(i: int) -> int:
        for j in range(i - 1, -1, -1):
            if T[j][2] < T[i][1]:
                return j

        return -1

    for h, a, b, w in T:
        X.append((h, a, b, w, h * (b - a)))
    X.append((-1, -1, -1, -1, -1))
    T = X
    # print(T)

    # DP[0] = [T[0][4] for _ in range(p + 1)]

    n = len(T)

    DP = [[-1 for _ in range(p + 1)] for _ in range(n)]
    parent = [[None for _ in range(p + 1)] for _ in range(n)]
    taken = [False for _ in range(n)]
    T.sort(key=lambda x: x[2])
    DP[0] = [0 for _ in range(p + 1)]
    # print(T)

    for i in range(1, n):
        for j in range(p + 1):
            if j - T[i][3] >= 0:
                # print(i,j,DP[i-1][p],T[i][4] + DP[prev(i)][j - T[i][3]])
                # DP[i][j] = max(DP[i - 1][p], T[i][4] + DP[prev(i)][j - T[i][3]])
                DP[i][j] = DP[i - 1][p]
                for k in range(i - 1, -1, -1):
                    if T[k][2] < T[i][1]:
                        DP[i][j] = max(DP[i][j], T[i][4] + DP[k][j - T[i][3]])

    def rek(i: int, t: int):

        if i < 0 or t < 0:
            return 0

        if DP[i][t] != -1:
            return DP[i][t]

        # result1 = rek(i - 1, t)
        # result2 = -1
        # result2 = T[i][4] + rek(prev(i), t - T[i][3])
        # # if t - T[i][3] >= 0:
        # #     for j in range(i - 1, -1, -1):
        # #         if T[j][2] < T[i][1]:
        # #             result2 = max(result2, T[i][4] + rek(j, t - T[i][3]))
        # #             break
        # if result1 > result2:
        #     DP[i][t] = result1
        # else:
        #     DP[i][t] = result2

        # DP[i][t] = max(rek(i - 1, t), T[i][4] + rek(prev(i), t - T[i][3]))

        return DP[i][t]

    # for i in range(p,-1,-1):
    #     rek(n - 1, i)

    best = -1
    for i in DP:
        for j in i:
            best = max(best, j)
    print(max(DP[-1]), best, "output")
    # print(DP)
    # print(DP)
    # print(taken)
    return [0]


runtests(select_buildings)

T = [(2, 1, 5, 3),
     (3, 7, 9, 2),
     (2, 8, 11, 1)]
p = 5
select_buildings(T, p)
