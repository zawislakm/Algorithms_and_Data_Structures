from egzP6btesty import runtests


def jump(M):
    # tutaj proszę wpisać własną implementację
    DP = {}
    x = y = 0
    DP[(x, y)] = True
    for el in M:
        if "UL" == el:
            x, y = x - 1, y + 2
        elif "UR" == el:
            x, y = x + 1, y + 2
        elif "RU" == el:
            x, y = x + 2, y + 1
        elif "RD" == el:
            x, y = x + 2, y - 1
        elif "DR" == el:
            x, y = x + 1, y - 2
        elif "DL" == el:
            x, y = x - 1, y - 2
        elif "LD" == el:
            x, y = x - 2, y - 1
        elif "LU" == el:
            x, y = x - 2, y + 1

        if (x, y) in DP:
            DP.pop((x, y))
        else:
            DP[(x, y)] = True

    return len(DP)


runtests(jump, all_tests=True)

M = ['UL', 'RD', 'LU', 'LU', 'RD', 'DL', 'UR', 'DR']
print(jump(M))
