# longest increasing subsequence


def lis(A: list) -> int:
    n = len(A)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]  # parent list

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                P[i] = j
                F[i] = F[j] + 1

    path = []

    def find_lis(i: int) -> None:
        if P[i] != -1:
            find_lis(P[i])
        path.append(A[i])

    best = -1
    index = -1
    for i, e in enumerate(F):
        if e > best:
            best = e
            index = i

    find_lis(index)
    print(f"Found solution is: {path}, length: {F[index]}")

    return F[index]


A = [2, 1, 4, 3, 1, 5, 2, 7, 8, 3]
lis(A)
