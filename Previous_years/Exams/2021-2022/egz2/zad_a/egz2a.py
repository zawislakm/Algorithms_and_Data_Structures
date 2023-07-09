from egz2atesty import runtests


def acceptable_solution(A: list, T: int) -> int:
    n = len(A)
    M = [0 for _ in range(n)]

    ans = -1
    for c in A:
        for i in range(n):
            if M[i] + c <= T:
                M[i] += c
                ans = i
                break

    return ans


def coal(A, T):
    # tu prosze wpisac wlasna implementacje

    return acceptable_solution(A, T)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(coal, all_tests=True)
