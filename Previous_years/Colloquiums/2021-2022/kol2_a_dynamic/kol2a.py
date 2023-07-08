from kol2atesty import runtests

"""
nlogn solition

F(i,d) = minimalna liczba puntków kontrolnych przez które prowadzi Marian, gdy dojezdza do i-tego punktu, a za 
        kierownica siedzi kierowaca d
        
i - punkt przesiadkowy
d - kierowaca (0 - Marian, 1- Jacek)

f(i,M) = min( F(i-1,J) + C[i-1,i], F(i-2,J) + C[i-2,i], F(i-3,J) + C[i-3,i])
C[i-1,i] liczba punktów kontorlnych miedzy pozycja i-1 oraz i
f(i,J) =  min( F(i-1,M),F(i-1,M),F(i-1,M)) 

f(0,M) = 0
f(0,J) = inf


Tablice z punktami kontrlnym oraz przesiadkowymi została zamianieona na tablie z jedynie puntkami przesiadkowymi
z (ich indexem na osi, z iloscia punktów kotnrolnych od startu, indexem w tabeli P).

Dynamik wraz z odtworzeniem trasy
"""

INF = 10 ** 10


def drivers(P: list, B: int) -> list:
    X = []
    for i, (e, v) in enumerate(P):
        X.append((e, v, i))
    P = X

    P.sort(key=lambda x: x[0])
    T = [(0, 0, -1)]
    control_points = 0

    for i, f, index in P:

        if f is False:
            control_points += 1
        else:
            T.append((i, control_points, index))
    T.append((B, control_points, -1))

    n = len(T)

    DP = [[INF for _ in range(2)] for _ in range(n)]
    parent = [[None for _ in range(2)] for _ in range(n)]
    DP[0][1] = INF
    DP[0][0] = 0

    # d = 0 Marian, d = 1 Jacek

    for i in range(1, n):
        j = 1
        while j < 4 and i - j >= 0:
            # d == 1
            result = DP[i - j][0]
            if result < DP[i][1]:
                DP[i][1] = result
                parent[i][1] = i - j

            # d == 0
            result = DP[i - j][1] + (T[i][1] - T[i - j][1])

            if result < DP[i][0]:
                DP[i][0] = result
                parent[i][0] = i - j
            j += 1

    # recursive version doesnt work on test 9
    # def rek(i: int, d: int) -> int:
    #     if i < 0:
    #         return 0
    #
    #     if i == 0 and d == 1:
    #         return INF
    #     if DP[i][d] != INF:
    #         return DP[i][d]
    #     if d == 1:
    #         j = 1
    #         while j < 4 and i - j >= 0:
    #             result = rek(i - j, 0)
    #             if result < DP[i][d]:
    #                 DP[i][d] = result
    #                 parent[i][d] = i - j
    #             j += 1
    #     else:
    #
    #         j = 1
    #         while j < 4 and i - j >= 0:
    #             result = rek(i - j, 1) + (T[i][1] - T[i - j][1])
    #
    #             if result < DP[i][d]:
    #                 DP[i][d] = result
    #                 parent[i][d] = i - j
    #             j += 1
    #
    #     return DP[i][d]
    #
    # rek(n - 1, 0)
    # rek(n - 1, 1)

    path = []
    person = DP[-1].index(min(DP[-1]))
    pointer = parent[-1][person]

    while pointer != None:
        path.append(T[pointer][2])
        person = 1 - person
        pointer = parent[pointer][person]

    path.remove(-1)

    return path


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(drivers, all_tests=True)

p = True
c = False

P = [(1, c), (3, c), (4, c), (6, c), (8, c), (9, c), (11, c), (13, c), (16, c), (17, c),
     (2, p), (5, p), (7, p), (10, p), (12, p), (14, p), (15, p), (18, p)]

B = 20
drivers(P, B)
