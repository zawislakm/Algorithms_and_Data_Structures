"""
Type of coins and the price is given. Infinite number of coins. Find minimal number coins to pay.
Return the list of coins used.
"""

"""
Depending on the condition of task can be solve using greedy or dynamic approach
Greedy works when 2 conditions are matched:
1. There is 1 in coins
2. ci >= 2* ci-1, i and i-1 means index in list of coins in sorted array

Greedy simply pick biggest possible coin till its possible, than change to next possible coin

Otherwise dynamic solution need to be used:

F(i) = minimal number of coins to pay price equal i
F(i) = min(F(i-c)+1), c in coins and i >= c
"""
INF = 10 ** 10


def dynamic(coins: list, price: int) -> list:
    print("Dynamic start")
    DP = [INF for _ in range(price + 1)]
    parent = [-1 for _ in range(price + 1)]
    parent[0] = DP[0] = 0

    def rek(i: int) -> int:

        if DP[i] != INF:
            return DP[i]

        for c in coins:
            if i >= c:
                result = 1 + rek(i - c)
                if result < DP[i]:
                    DP[i] = result
                    parent[i] = c

        return DP[i]

    rek(price)
    used = []
    while price > 0:
        used.append(parent[price])
        price -= parent[price]
    return used


def greedy(coins: list, price: int) -> list:
    print("Greedy start")
    used = []
    coins.reverse()
    i = 0
    while price > 0 and i < len(coins):

        if price - coins[i] >= 0:
            used.append(coins[i])
            price -= coins[i]
        else:
            i += 1

    return used if price == 0 else None


def task(coins: list, price: int) -> list:
    coins.sort()

    if 1 in coins:
        for i in range(1, len(coins)):
            if coins[i] < 2 * coins[i - 1]:
                return dynamic(coins, price)
    else:
        return dynamic(coins, price)
    return greedy(coins, price)


coins = [1, 2, 5]
price = 19
print(f'Used this coins {task(coins, price)}')
