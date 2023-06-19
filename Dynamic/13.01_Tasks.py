# greedy
# picking task which ends earlier
def tasks(T: list) -> int:
    T.sort(key=lambda x: (x[1], x[0]))
    tasks_taken = last_end = 0

    for s, t in T:
        if last_end <= s:
            tasks_taken += 1
            last_end = t
    return tasks_taken


T = [(0, 2), (0, 1), (0, 3), (2, 4), (4, 5), (4, 6), (5, 7)]
tasks(T)
