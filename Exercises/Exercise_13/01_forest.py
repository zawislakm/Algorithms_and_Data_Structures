"""
Find maximal sum of cut trees, cutting trees next to each other is forbidden
"""

"""
Take tree and skip next one or skip tree now

F(i) = T[0] i == 0
F(i) = max(T[0],T[1]) i == 1
F(i) = max(T+F[i-2], F[i-1]) i != 0 and i != 1

F(i) = 0 i<0

F(i) = the maximum number of trees that can be reached by considering the first and trees

Other solution:
F(i) = T[0] i == 0
F(i) = T[1] i == 1
F(i) = T[2] + T[0] i == 2 
F(i) = T[i] + max(F[i-2] + F[i-3]) i != 0 and i != 1
"""

def forest(T: list) -> int:
    n = len(T)

    F = [-1 for _ in range(n)]
    F[0] = T[0]
    F[1] = T[1]

    def cutter(i: int = len(T) - 1) -> int:
        nonlocal T, F

        if i == 0:
            return F[0]
        if i == 1:
            return max(F[0], F[1])

        if F[i] != -1:
            return F[i]

        F[i] = max(T[i] + cutter(i - 2), cutter(i - 1))
        return F[i]

    cutter()
    print(F)
    return F[-1]


T = [5, 1, 1, 5]
forest(T)
