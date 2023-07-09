from zad9testy import runtests

"""
F(i,u) - minimalny koszt dojazdu do parking i, mogą lub nie mogąc wykorzystać zasadu 2T
i - parking
u - uzycie zasady 2T (u =1 mozna korzystac, u=0 nie mozna korzystac)


F(i,0) = min( F(j,0) + C[i]), gdzie j nalezy 0 < O[i] - O[j] < T


F(i,1) = min ( min (F(j,0) + C[i]) gdzie j nalezy T <= O[i] - O[j] <= 2T lub
               min (F(j,1) + C[i]) gdzie j nalezy do 0 < O[i] - O[j] < T)
                
Warto dodać parking A oraz B z kosztem 0


O(nlogn) solution means using 3 min heaps

"""

INF = 10 ** 10


def min_cost(O: list, C: list, T: int, L: int) -> int:
    # O(n^2)
    P = [i for i in zip(O, C)]
    P.append((0, 0))
    P.append((L, 0))
    P.sort(key=lambda x: x[0])
    n = len(P)
    DP = [[INF for _ in range(2)] for _ in range(n)]
    DP[0] = [0, 0]

    for i in range(1, n):
        x0 = x1 = INF
        for j in range(i - 1, -1, -1):
            if P[i][0] - P[j][0] > 2 * T:
                break
            elif P[i][0] - P[j][0] <= T:
                # not using 2T cheat
                x0 = min(DP[j][0], x0)
                x1 = min(DP[j][1], x1)
            else:
                # using 2T cheat
                x1 = min(DP[j][0], x1)
        DP[i] = [x0 + P[i][1], x1 + P[i][1]]

    return DP[-1][1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=False)

O = [17, 20, 11, 5, 12]  # pozycje parkingów
C = [9, 7, 7, 7, 3]  # koszt pargingów
T = 7
L = 25
min_cost(O, C, T, L)
