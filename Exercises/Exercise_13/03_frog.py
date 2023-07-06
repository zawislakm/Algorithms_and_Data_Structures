"""
Monica the frog jumps over leaves with snacks. By eating the snack he gains energy.
The task is to minimize the frog's jumps. Jump t leafs ahead cost t^2 energy.
"""

"""
F(i,a) - minmalna liczba skoków zeby dostac sie na ite pole oraz miec a kaolrii w zapasie

z pola j na i to musi miec a + (i-j)^2 - P[j]  kalorii


"""

#doesnt work!
INF = 100


def frog(P):
    n = len(P)
    A = sum(P)

    F = [[INF for _ in range(n ** 2)] for _ in range(n)]
    F[0] = [0 for _ in range(n ** 2)]

    def jump(i: int, a):
        nonlocal P
        # print(i,a)
        # if i == 0:
        #     return 0

        if F[i][a] != INF:
            return F[i][a]

        for j in range(i-1,-1,-1):
            if a + (i - j) ** 2 - P[j] >= 0:
                F[i][a] = min(jump(j, a + (i - j) ** 2 - P[j]) + 1, F[i][a])

        return F[i][a]

    for a in range(A):
        jump(n - 1, a)

    for i in F:
        print(i)


    print(F[-1])


P = [11, 0, 0, 5, 0, 7, 0, 3, 1, 0]
frog(P)
