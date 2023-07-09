from egz3atesty import runtests

"""
O(nT) 


other solutions needs segments tree
"""


def snow(T: int, I: list) -> int:
    # tu prosze wpisac wlasna implementacje

    road = [0 for _ in range(T + 1)]

    for u, v in I:

        for i in range(u, v + 1):
            road[i] += 1

    return max(road)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
