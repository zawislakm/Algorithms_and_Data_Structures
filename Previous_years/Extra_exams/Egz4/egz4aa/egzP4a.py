from egzP4atesty import runtests

"""
Dynamik
LIS idea. Trzeba posrtowac po pierwszej a potem drugiej wspolrzednej. Mozna brac most jezeli wspolrzedna koncowac
naszego mostu jest wieksza badz rowna od konca wczesniejszego mostu.


Mozna to przyspieszycz do mlogn uzywacj binsearch do znajdywania mostu
"""


def mosty(T: list) -> int:
    # tutaj proszę wpisać własną implementację
    T.sort(key=lambda x: (x[0], x[1]))
    # print(T)
    n = len(T)
    DP = [1 for _ in range(n)]
    DP[0] = 1

    for i in range(1, n):

        for j in range(i):
            # if i ==5 and j == 4:
            # print(T[i],T[j],T[j][0] < T[i][1])
            if T[j][1] <= T[i][1] and DP[i] < DP[j] + 1:
                DP[i] = DP[j] + 1

    # print(DP)
    return max(DP)


runtests(mosty, all_tests=True)

T = [(8, 1), (1, 2), (4, 3), (3, 4), (5, 5), (2, 6), (6, 7), (7, 8)]
mosty(T)
