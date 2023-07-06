# Knapsack again :)
"""
Knapsack with weight, height and price
"""

"""
2 dimension array, iterate each element, each time from the back of dynamic array. 
"""


def knapsack(T, w, h):
    n = len(T)
    dp = [[-1000 for _ in range(w + 1)] for _ in range(h + 1)]
    dp[0][0] = 0
    P = [[-1 for _ in range(w + 1)] for _ in range(h + 1)]  # parent array

    for k in range(n):  # elements loop
        for i in range(h - 1, -1, -1):  # height loop
            for j in range(w - 1, -1, -1):  # weight loop

                if dp[i][j] > -1000 and i + T[k][1] < h + 1 and j + T[k][0] < w + 1:
                    if dp[i + T[k][1]][j + T[k][0]] < dp[i][j] + T[k][2]:
                        dp[i + T[k][1]][j + T[k][0]] = dp[i][j] + T[k][2]
                        P[i + T[k][1]][j + T[k][0]] = k

    # finding maximal value with it position
    cost = -1001
    position = (-1, -1)
    for i in range(h + 1):
        for j in range(w + 1):
            if dp[i][j] > cost:
                cost = dp[i][j]
                position = (i, j)

    # finding which elements where stolen
    elements = []
    while position[0] > 0 and position[1] > 0:
        elem = P[position[0]][position[1]]
        elements.append(T[elem])
        position = (position[0] - T[elem][1], position[1] - T[elem][0])

    print(f'Stolen things {elements}')

    return cost


T = [(3, 5, 2), (1, 1, 10), (4, 1, 8), (7, 2, 1)]  # w,h,c
w = 7
h = 7
print(knapsack(T, w, h))
