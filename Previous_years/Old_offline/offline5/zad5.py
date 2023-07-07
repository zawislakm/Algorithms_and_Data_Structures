from zad5testy import runtests
import queue
"""
Greedy 
"""

def plan(T: list) -> list:
    stops = []
    Q = queue.PriorityQueue()

    oil = 0
    n = len(T)
    last_look = -1
    while oil < n - 1:

        for i in range(last_look + 1, min(oil + 1, n)):
            Q.put((-1 * T[i], i))
            last_look = i

        station_oil, station_position = Q.get()

        oil += -1 * station_oil
        stops.append(station_position)

    stops.sort()
    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)

T = [3, 0, 2, 1, 0, 2, 5, 0]
plan(T)
