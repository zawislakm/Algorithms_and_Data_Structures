from egz1atesty import runtests


def snow(S: list) -> int:
    # tu prosze wpisac wlasna implementacje
    S.sort(reverse=True)
    ans = 0
    for i, s in enumerate(S):
        if s - i <= 0:
            break
        ans += s - i
    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
